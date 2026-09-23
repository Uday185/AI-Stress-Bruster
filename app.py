"""
MindEase - AI-Powered Stress Relief and Book Recommendation System
A comprehensive application that analyzes user stress, extracts keywords, 
and recommends philosophical and ethical books for relief.
"""

from flask import Flask, render_template, request, jsonify
import sqlite3
import random
import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import keyword extractor
try:
    from keyword_extractor import extract_keywords, extract_phrases, get_keyword_sentiment
    KEYWORD_EXTRACTION_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import keyword_extractor: {e}")
    KEYWORD_EXTRACTION_AVAILABLE = False
    def extract_keywords(text, max_keywords=10):
        return text.split()[:max_keywords]
    def extract_phrases(text, min_phrase_length=2):
        return []
    def get_keyword_sentiment(keywords):
        return {"sentiment": "neutral", "intensity": "moderate"}

app = Flask(__name__)


# ==================== STRESS CLASSIFICATION ====================

def classify_stress(text, keywords=None):
    """
    Classify stress type based on text and extracted keywords.
    Uses both text matching and keyword analysis.
    
    Args:
        text: User input text
        keywords: Pre-extracted keywords (optional)
        
    Returns:
        Classified stress type
    """
    text = text.lower()
    
    # Extract keywords if not provided
    if keywords is None:
        keywords = extract_keywords(text)
    
    keywords_str = " ".join(keywords).lower()
    combined_text = text + " " + keywords_str

    # Emergency detection (HIGHEST PRIORITY)
    emergency_terms = ["suicide", "kill myself", "end my life", "i want to die", 
                      "hopeless", "self harm", "end it", "not worth living"]
    if any(term in combined_text for term in emergency_terms):
        return "emergency"

    # Career stress (check before anxiety since "boss stress" should be career)
    career_terms = ["career", "job", "jobs", "promotion", "boss", "work",
                   "workplace", "office", "employment", "unemployed", "interview",
                   "resignation", "professional", "career change", "job loss",
                   "coworker", "work stress", "work pressure"]
    if any(term in combined_text for term in career_terms):
        return "career"

    # Financial stress (check before anxiety since "money worry" should be financial)
    financial_terms = ["money", "financial", "finance", "debt", "bills",
                      "budget", "expensive", "poor", "afford", "income",
                      "salary", "payment", "broke", "economical", "cost",
                      "spending", "financial stress"]
    if any(term in combined_text for term in financial_terms):
        return "financial"

    # Academic stress
    academic_terms = ["exam", "exams", "marks", "grades", "study", "studies",
                     "assignment", "assignments", "college", "school", "university",
                     "test", "thesis", "project", "presentation", "quiz", "homework",
                     "coursework", "academic", "class", "lecture"]
    if any(term in combined_text for term in academic_terms):
        return "academic"

    # Anxiety
    anxiety_terms = ["anxious", "anxiety", "panic", "overthinking", "worry",
                    "worried", "nervous", "stress", "overwhelmed", "pressure",
                    "tense", "restless", "uneasy"]
    if any(term in combined_text for term in anxiety_terms):
        return "anxiety"

    # Emotional/Depression
    emotional_terms = ["sad", "crying", "cried", "heartbroken", "depressed",
                      "depression", "grief", "grieving", "empty", "miserable", 
                      "unhappy", "down", "blue", "melancholy"]
    if any(term in combined_text for term in emotional_terms):
        return "emotional"

    # Loneliness (check before general social/family)
    loneliness_terms = ["lonely", "loneliness", "isolated", "isolation", "no friends",
                       "nobody", "alone", "solitude", "disconnected", "no one"]
    if any(term in combined_text for term in loneliness_terms):
        return "loneliness"

    # Family stress
    family_terms = ["family", "parent", "parents", "father", "mother", "sibling",
                   "brother", "sister", "family conflict", "family issues", "home",
                   "relative", "relatives", "household", "family problem"]
    if any(term in combined_text for term in family_terms):
        return "family"

    # Confidence issues
    confidence_terms = ["confidence", "confident", "self-doubt", "insecure",
                       "shy", "awkward", "timid", "uncertain"]
    if any(term in combined_text for term in confidence_terms):
        return "confidence"

    # Social anxiety
    social_terms = ["social", "socializing", "friends", "party", "parties",
                   "meeting people", "talk to people", "conversation", "interaction",
                   "social event", "gathering", "social skills"]
    if any(term in combined_text for term in social_terms):
        return "social"

    # Breakup/Relationship loss (romantic)
    breakup_terms = ["breakup", "broke up", "heartbreak", "broken heart", "ex",
                    "dumped", "divorce", "separated", "lost my boyfriend", 
                    "lost my girlfriend", "ex-partner"]
    if any(term in combined_text for term in breakup_terms):
        return "breakup"

    # Health stress
    health_terms = ["health", "sick", "illness", "disease", "doctor", "medical",
                   "diagnosis", "treatment", "hospital", "pain", "injury", "healthcare"]
    if any(term in combined_text for term in health_terms):
        return "health"

    # Peer pressure
    peer_terms = ["peer pressure", "peer influence", "people judge", "what people think",
                 "fitting in", "belong", "popular", "bullied", "teased", "outsider"]
    if any(term in combined_text for term in peer_terms):
        return "peer-pressure"

    # Relationship stress (romantic/partner - different from breakup)
    relationship_terms = ["relationship", "boyfriend", "girlfriend", "husband", "wife",
                         "partner", "dating", "marriage", "argument", "fights",
                         "trust issues", "communication", "spouse"]
    if any(term in combined_text for term in relationship_terms):
        return "relationship"

    # Self-esteem
    self_esteem_terms = ["self-esteem", "self esteem", "self-worth", "self worth",
                        "worthless", "not good enough", "compare", "inferior",
                        "rejected", "inadequate"]
    if any(term in combined_text for term in self_esteem_terms):
        return "self-esteem"

    # Time management
    time_terms = ["time management", "deadline", "deadlines", "procrastinate",
                 "procrastination", "too much work", "busy", "schedule", "organize",
                 "rushing", "time pressure"]
    if any(term in combined_text for term in time_terms):
        return "time-management"

    # Self-doubt/Impostor syndrome
    self_doubt_terms = ["impostor", "imposter", "fake", "fraud", "don't deserve",
                       "not qualified", "can't do", "not smart enough", "self-critic",
                       "perfectionist", "inadequate", "not enough"]
    if any(term in combined_text for term in self_doubt_terms):
        return "self-doubt"

    # Default
    return "general"


# ==================== DATABASE OPERATIONS ====================

def load_books(stress_type=None):
    """
    Load books from the local database.

    Args:
        stress_type: Optional filter for specific stress type

    Returns:
        List of books
    """
    try:
        # Always resolve db relative to this file (so running Flask from anywhere works)
        app_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(app_dir, "library.db")

        if not os.path.exists(db_path):
            # Fallbacks (in case library.db is placed elsewhere)
            fallback_paths = [
                os.path.join(os.getcwd(), "library.db"),
                os.path.join(app_dir, "..", "library.db"),
                os.path.join(os.path.dirname(app_dir), "library.db"),
            ]
            found = next((p for p in fallback_paths if os.path.exists(p)), None)
            if found is None:
                print("Error: Database 'library.db' not found. Looked for:", [db_path] + fallback_paths)
                return []
            db_path = found

        print(f"✓ Loading database from: {db_path}")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        if stress_type:
            cursor.execute("""
                SELECT stress_type, title, author, chapter,
                       chapter_summary, content, shelf, availability, priority
                FROM books
                WHERE stress_type = ?
            """, (stress_type,))
        else:
            cursor.execute("""
                SELECT stress_type, title, author, chapter,
                       chapter_summary, content, shelf, availability, priority
                FROM books
            """)

        books = cursor.fetchall()
        conn.close()
        return books

    except Exception as e:
        print(f"Database Error: {e}")
        return []


def get_local_recommendation(stress_type):
    """
    Get book recommendation from local database for a specific stress type.
    
    Args:
        stress_type: Type of stress
        
    Returns:
        Dictionary with book details or None
    """
    books = load_books(stress_type)

    # Filter available books
    available = [
        book for book in books
        if book[6].lower() == "available"
    ]

    if not available:
        # Return any book if none marked available
        if books:
            available = books
        else:
            return None

    # Sort by priority (lower = higher priority)
    available.sort(key=lambda x: x[7] if x[7] else 999)
    
    # Get books with highest priority
    top_priority = available[0][7] if available[0][7] else 999
    top_books = [book for book in available if (book[7] or 999) == top_priority]

    # Randomly select from top priority books.
    # To avoid returning the same book repeatedly for the same stress type,
    # try to pick a different book each time by rotating based on a per-process counter.
    if not hasattr(get_recommendation, "_rotation_counter"):
        get_recommendation._rotation_counter = 0  # type: ignore[attr-defined]

    get_recommendation._rotation_counter += 1  # type: ignore[attr-defined]
    start_idx = get_recommendation._rotation_counter % max(len(top_books), 1)
    rotated = top_books[start_idx:] + top_books[:start_idx]
    selected = rotated[0]


    return {
        "title": selected[1],
        "author": selected[2],
        "chapter": selected[3],
        "chapter_summary": selected[4],
        "content": selected[5],
        "shelf": selected[6],
        "availability": selected[7],
        "stress_type": selected[0]
    }


def get_recommendation(stress_type):
    """
    Get book recommendation - uses local database.
    
    Args:
        stress_type: Type of stress
        
    Returns:
        Tuple: (recommendation dict, source)
    """
    recommendation = get_local_recommendation(stress_type)
    
    if recommendation:
        return recommendation, "local"
    
    return None, "none"


# ==================== MOTIVATION & SUPPORT ====================

def get_motivation(stress_type):
    """
    Get motivational and supportive message for the stress type.
    
    Args:
        stress_type: Type of stress
        
    Returns:
        Motivational message
    """
    messages = {
        "academic": "🎯 Focus on progress, not perfection. Every small step counts toward your goal. Break your studies into manageable chunks and celebrate each accomplishment.",
        "anxiety": "🌸 Breathe slowly and deeply. This feeling will pass. You are stronger than you think. Take things one moment at a time.",
        "emotional": "💪 Pain is temporary. Stay strong - this too shall pass. Allow yourself to feel, but remember: you have the strength to persevere.",
        "career": "🌱 Growth takes time. Keep learning and evolving - your career journey is unique. Every challenge is an opportunity to grow.",
        "financial": "💰 Focus on what you can control. Small financial habits lead to big changes. You have the power to improve your situation.",
        "family": "🏠 Family bonds are complex but enduring. Communication is key to understanding. Approach with patience and compassion.",
        "confidence": "⭐ You are capable of amazing things. Believe in yourself! Your potential is limitless.",
        "social": "🤝 Start with small conversations. Everyone appreciates genuine connection. You are worthy of meaningful relationships.",
        "loneliness": "💙 You matter. Reach out - there are people who care about you. Connection begins with one small step.",
        "breakup": "❤️ Heartbreak hurts, but it makes room for new beginnings. Heal at your own pace. Your worth isn't determined by anyone else.",
        "health": "🏥 Your health is your wealth. Take it one day at a time. You are taking the right steps toward healing.",
        "peer-pressure": "✨ Stay true to yourself. Your values define you, not others' opinions. Your authenticity is your strength.",
        "relationship": "💑 Relationships take work. Communication and respect are foundations. You deserve a partnership built on understanding.",
        "self-esteem": "🌟 You are worthy exactly as you are. Embrace your unique self. Your imperfections make you beautifully human.",
        "time-management": "⏰ Break big tasks into small ones. Focus on one thing at a time. Progress is made one step at a time.",
        "self-doubt": "🌈 You belong here. Your achievements are real - own your success! You have already overcome so much.",
        "general": "🌻 Every challenge carries the seed of opportunity. You've got this! Take a deep breath and remember your resilience.",
        "emergency": "⚠️ YOU MATTER DEEPLY. PLEASE REACH OUT FOR IMMEDIATE HELP:\n\n📞 National Suicide Prevention Lifeline: 988 (US)\n📞 Crisis Text Line: Text HOME to 741741\n🌍 International Association for Suicide Prevention: https://www.iasp.info/resources/Crisis_Centres/\n\n❤️ PLEASE talk to someone you trust or contact a mental health professional RIGHT NOW. Your life is valuable, and help is available."
    }

    return messages.get(stress_type, messages["general"])


# ==================== ROUTES ====================

@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    """Analyze user input and provide recommendations."""
    user_input = request.form.get("stress", "").strip()

    if not user_input:
        return render_template("result.html",
                               error="Please enter your concern or feeling.")

    # Extract keywords and phrases
    keywords = extract_keywords(user_input) if KEYWORD_EXTRACTION_AVAILABLE else []
    phrases = extract_phrases(user_input) if KEYWORD_EXTRACTION_AVAILABLE else []
    sentiment = get_keyword_sentiment(keywords) if KEYWORD_EXTRACTION_AVAILABLE else {}

    # Ensure template-safe sentiment object (prevents missing-key template errors)
    if not sentiment:
        sentiment = {}
    sentiment.setdefault("sentiment", "neutral")
    sentiment.setdefault("intensity", "moderate")
    sentiment.setdefault("negative_keywords", [])


    # Classify stress type
    stress_type = classify_stress(user_input, keywords)
    print(f"✓ User input: {user_input[:80]}...")
    print(f"✓ Keywords extracted: {keywords}")
    print(f"✓ Sentiment: {sentiment.get('sentiment', 'N/A')}")
    print(f"✓ Classified stress type: {stress_type}")

    # Handle emergency
    if stress_type == "emergency":
        return render_template("result.html",
                               stress_type="🚨 EMERGENCY SUPPORT",
                               recommendation=None,
                               motivation=get_motivation("emergency"),
                               keywords=keywords,
                               sentiment=sentiment)

    # Get recommendation
    recommendation, source = get_recommendation(stress_type)
    motivation = get_motivation(stress_type)

    return render_template("result.html",
                           stress_type=stress_type.capitalize().replace("-", " "),
                           recommendation=recommendation,
                           source=source,
                           motivation=motivation,
                           keywords=keywords,
                           phrases=phrases,
                           sentiment=sentiment)


@app.route("/api/keywords", methods=["POST"])
def api_keywords():
    """API endpoint to extract keywords from text."""
    data = request.get_json()
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    keywords = extract_keywords(text)
    phrases = extract_phrases(text)
    sentiment = get_keyword_sentiment(keywords)
    
    return jsonify({
        "keywords": keywords,
        "phrases": phrases,
        "sentiment": sentiment
    })


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return render_template("error.html", message="Page not found"), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return render_template("error.html", message="Internal server error"), 500


# ==================== MAIN ====================

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🧠 MindEase - Stress Relief and Book Recommendation System")
    print("=" * 70)
    print(f"✓ Keyword extraction: {'Available' if KEYWORD_EXTRACTION_AVAILABLE else 'Unavailable'}")
    print("✓ Flask server starting...")
    print("✓ Access at: http://localhost:5000")
    print("=" * 70 + "\n")
    app.run(debug=True)
