# -*- coding: utf-8 -*-
"""
OpenAlex Client Module
Fetches books from OpenAlex API based on stress categories
"""

import requests
import json


# Mapping stress categories to OpenAlex concept IDs for relevant topics
STRESS_CONCEPTS = {
    "academic": [
        "academic stress",
        "study skills",
        "exam anxiety",
        "academic performance",
        "student stress"
    ],
    "anxiety": [
        "anxiety",
        "anxiety disorder",
        "generalized anxiety",
        "stress management",
        "panic disorder"
    ],
    "emotional": [
        "emotional regulation",
        "emotional intelligence",
        "depression",
        "emotional health",
        "mood disorders"
    ],
    "career": [
        "career development",
        "job stress",
        "occupational stress",
        "career guidance",
        "professional development"
    ],
    "financial": [
        "financial stress",
        "financial literacy",
        "money management",
        "personal finance",
        "financial planning"
    ],
    "family": [
        "family relationships",
        "family stress",
        "family dynamics",
        "parenting stress",
        "family conflict"
    ],
    "confidence": [
        "self confidence",
        "self esteem",
        "self efficacy",
        "self worth",
        "confidence building"
    ],
    "social": [
        "social skills",
        "social anxiety",
        "interpersonal relationships",
        "social support",
        "communication skills"
    ],
    "loneliness": [
        "loneliness",
        "social isolation",
        "social connection",
        "social belonging",
        "isolation"
    ],
    "breakup": [
        "breakup",
        "heartbreak",
        "relationship loss",
        "divorce",
        "separation"
    ],
    "health": [
        "health",
        "wellness",
        "health promotion",
        "disease prevention",
        "healthy lifestyle"
    ],
    "peer-pressure": [
        "peer pressure",
        "social influence",
        "conformity",
        "group pressure"
    ],
    "relationship": [
        "relationships",
        "romantic relationships",
        "relationship advice",
        "couples therapy",
        "dating"
    ],
    "self-esteem": [
        "self esteem",
        "self worth",
        "self acceptance",
        "self concept",
        "self love"
    ],
    "time-management": [
        "time management",
        "productivity",
        "procrastination",
        "organization",
        "efficiency"
    ],
    "self-doubt": [
        "impostor syndrome",
        "self doubt",
        "self criticism",
        "perfectionism",
        "inner critic"
    ],
    "general": [
        "self help",
        "personal development",
        "mental health",
        "psychology",
        "wellbeing"
    ],

    "emergency": [
    "crisis intervention",
    "suicide prevention",
    "mental health crisis",
    "emergency mental health",
    "psychological crisis support"
],
    
}


def search_openalex_books(stress_type, limit=5):
    """
    Search OpenAlex for books related to a stress category
    
    Args:
        stress_type: The stress category to search for
        limit: Maximum number of results to return
        
    Returns:
        List of book dictionaries with metadata
    """
    # Get search terms for this stress type
    search_terms = STRESS_CONCEPTS.get(stress_type, STRESS_CONCEPTS["general"])
    
    books = []
    
    for term in search_terms:
        results = _fetch_books_for_term(term, limit=limit)
        books.extend(results)
        
        if len(books) >= limit:
            break
    
    # Remove duplicates based on title
    seen_titles = set()
    unique_books = []
    for book in books:
        title_lower = book.get("title", "").lower()
        if title_lower not in seen_titles:
            seen_titles.add(title_lower)
            unique_books.append(book)
    
    return unique_books[:limit]


def _fetch_books_for_term(search_term, limit=5):
    """
    Fetch books from OpenAlex API for a specific search term
    
    Args:
        search_term: The term to search for
        limit: Maximum number of results
        
    Returns:
        List of book dictionaries
    """
    base_url = "https://api.openalex.org/works"
    
    # Search for works with type=book containing the search term
    params = {
        "filter": "type:book",
        "search": search_term,
        "per_page": limit,
        "sort": "cited_by_count:desc"  # Most cited first
    }
    
    headers = {
        "User-Agent": "StressReliefBookRecommender/1.0 (mailto:support@example.com)"
    }
    
    try:
        response = requests.get(base_url, params=params, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return _parse_books(data.get("results", []))
        else:
            print(f"OpenAlex API error: {response.status_code}")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return []


def _parse_books(results):
    """
    Parse OpenAlex results into a simplified book format
    
    Args:
        results: List of OpenAlex work objects
        
    Returns:
        List of simplified book dictionaries
    """
    books = []
    
    for work in results:
        # Extract authors
        authors = []
        if "authorships" in work:
            for auth in work.get("authorships", []):
                author_name = auth.get("author", {}).get("display_name", "")
                if author_name:
                    authors.append(author_name)
        
        # Extract publication year
        pub_year = work.get("publication_year", "N/A")
        
        # Extract publisher
        publisher = work.get("host_venue", {}).get("publisher", "")
        
        # Extract abstract (limited)
        abstract_index = work.get("abstract_inverted_index", {})
        abstract_text = ""

        if abstract_index:
            try:
                words = []
                for word, positions in abstract_index.items():
                    for pos in positions:
                        words.append((pos, word))
                words = sorted(words)
                abstract_text = " ".join([word for pos, word in words])[:500]
            except:
                abstract_text = ""

        # Check if open access
        is_oa = work.get("open_access", {}).get("is_oa", False)

        # Get DOI for more info
        doi = work.get("doi", "")

        # Get title
        title = work.get("display_name", "Untitled")

        book = {
            "title": title,
            "author": ", ".join(authors[:3]) if authors else "Unknown Author",
            "year": pub_year,
            "publisher": publisher,
            "abstract": abstract_text,
            "is_oa": is_oa,
            "doi": doi,
            "openalex_id": work.get("id", ""),
            "cited_by_count": work.get("cited_by_count", 0)
        }

        books.append(book)
    
    return books


def get_book_recommendations(stress_type, limit=3):
    """
    Get book recommendations for a stress type from OpenAlex
    
    Args:
        stress_type: The stress category
        limit: Number of recommendations to return
        
    Returns:
        List of book recommendations
    """
    books = search_openalex_books(stress_type, limit=limit)
    
    recommendations = []
    for i, book in enumerate(books):
        rec = {
            "title": book["title"],
            "author": book["author"],
            "chapter": f"Published {book['year']}",
            "content": _generate_recommendation_content(book),
            "shelf": "OpenAlex",
            "availability": "Open Access" if book["is_oa"] else "Subscription",
            "year": book["year"],
            "publisher": book["publisher"],
            "doi": book["doi"],
            "openalex_id": book["openalex_id"],
            "cited_by_count": book["cited_by_count"]
        }
        recommendations.append(rec)
    
    return recommendations


def _generate_recommendation_content(book):
    """
    Generate recommendation content for a book

    Args:
        book: Book dictionary

    Returns:
        String with recommendation details
    """
    content = f"[BOOK] Recommended Book from OpenAlex\n\n"
    content += f"Title: {book['title']}\n\n"
    content += f"Author(s): {book['author']}\n\n"
    content += f"Published: {book['year']}\n\n"

    if book.get("publisher"):
        content += f"Publisher: {book['publisher']}\n\n"

    if book.get("abstract"):
        content += f"Description: {book['abstract'][:300]}...\n\n"

    if book.get("is_oa"):
        content += "[OK] This book is available Open Access!\n\n"

    if book.get("cited_by_count", 0) > 0:
        content += f"[*] Cited by {book['cited_by_count']} scholarly works\n\n"

    content += "This book has been recommended based on its relevance to stress management and mental well-being topics."

    return content


# ---------------- STRESS CLASSIFICATION FUNCTION ----------------
def classify_stress(text):
    """
    Classify the user's text input into stress categories
    """
    text = text.lower()

    # Emergency detection (highest priority)
    if any(word in text for word in ["suicide", "kill myself", "end my life",
                                     "i want to die", "hopeless", "self harm"]):
        return "emergency"

    # Academic stress
    elif any(word in text for word in ["exam", "exams", "marks", "grades", "study",
                                       "studies", "assignment", "assignments", 
                                       "college", "school", "university", "test",
                                       "thesis", "project", "presentation", "quiz"]):
        return "academic"

    # Anxiety
    elif any(word in text for word in ["anxious", "anxiety", "panic", "overthinking",
                                       "worry", "worried", "nervous", "stress", 
                                       "overwhelmed", "pressure", "tense"]):
        return "anxiety"

    # Emotional/Depression
    elif any(word in text for word in ["sad", "crying", "cried", "heartbroken",
                                       "depressed", "depression", "grief", "grieving",
                                       "lonely", "alone", "empty", "hopeless", "miserable"]):
        return "emotional"

    # Career stress
    elif any(word in text for word in ["career", "job", "jobs", "promotion", "boss",
                                       "work", "workplace", "office", "employment",
                                       "unemployed", "interview", "resignation"]):
        return "career"

    # Financial stress
    elif any(word in text for word in ["money", "financial", "finance", "debt",
                                       "bills", "budget", "expensive", "poor", 
                                       "afford", "income", "salary"]):
        return "financial"

    # Family stress
    elif any(word in text for word in ["family", "parent", "parents", "father",
                                       "mother", "sibling", "brother", "sister",
                                       "family conflict", "family issues", "home"]):
        return "family"

    # Confidence issues
    elif any(word in text for word in ["confidence", "confident", "self-doubt",
                                       "insecure", "shy", "awkward"]):
        return "confidence"

    # Social anxiety
    elif any(word in text for word in ["social", "socializing", "friends",
                                       "party", "parties", "meeting people",
                                       "talk to people", "conversation"]):
        return "social"

    # Loneliness
    elif any(word in text for word in ["lonely", "loneliness", "isolated",
                                       "no friends", "nobody", "alone"]):
        return "loneliness"

    # Breakup/Relationship loss
    elif any(word in text for word in ["breakup", "broke up", "heartbreak",
                                       "broken heart", "ex", "dumped", "divorce",
                                       "separated", "lost my boyfriend", "lost my girlfriend"]):
        return "breakup"

    # Health stress
    elif any(word in text for word in ["health", "sick", "illness", "disease",
                                       "doctor", "medical", "diagnosis", "treatment"]):
        return "health"

    # Peer pressure
    elif any(word in text for word in ["peer pressure", "peer influence",
                                       "people judge", "what people think", "fitting in",
                                       "belong", "popular", "bullied", "teased"]):
        return "peer-pressure"

    # Relationship stress
    elif any(word in text for word in ["relationship", "boyfriend", "girlfriend",
                                       "husband", "wife", "partner", "dating",
                                       "marriage", "argument", "fights", "trust issues"]):
        return "relationship"

    # Self-esteem
    elif any(word in text for word in ["self-esteem", "self esteem", "self-worth",
                                       "self worth", "worthless", "not good enough",
                                       "compare", "inferior", "rejected"]):
        return "self-esteem"

    # Time management
    elif any(word in text for word in ["time management", "time", "deadline",
                                       "deadlines", "procrastinate", "procrastination",
                                       "too much work", "busy", "schedule", "organize"]):
        return "time-management"

    # Self-doubt/Impostor syndrome
    elif any(word in text for word in ["impostor", "imposter", "fake", "fraud",
                                       "don't deserve", "not qualified", "can't do",
                                       "not smart enough", "self-critic", "perfectionist"]):
        return "self-doubt"

    else:
        return "general"


# ---------------- MOTIVATION MESSAGES ----------------
def get_motivation(stress_type):
    """Get motivation message for the stress type"""
    messages = {
        "academic": "[*] Focus on progress, not perfection. Every small step counts toward your goal.",
        "anxiety": "[*] Breathe slowly and deeply. This feeling will pass. You are stronger than you think.",
        "emotional": "[*] Pain is temporary. Stay strong - this too shall pass.",
        "career": "[*] Growth takes time. Keep learning and evolving - your career journey is unique.",
        "financial": "[*] Focus on what you can control. Small financial habits lead to big changes.",
        "family": "[*] Family bonds are complex but enduring. Communication is key to understanding.",
        "confidence": "[*] You are capable of amazing things. Believe in yourself!",
        "social": "[*] Start with small conversations. Everyone appreciates genuine connection.",
        "loneliness": "[*] You matter. Reach out - there are people who care about you.",
        "breakup": "[*] Heartbreak hurts, but it makes room for new beginnings. Heal at your own pace.",
        "health": "[*] Your health is your wealth. Take it one day at a time.",
        "peer-pressure": "[*] Stay true to yourself. Your values define you, not others' opinions.",
        "relationship": "[*] Relationships take work. Communication and respect are foundations.",
        "self-esteem": "[*] You are worthy exactly as you are. Embrace your unique self.",
        "time-management": "[*] Break big tasks into small ones. Focus on one thing at a time.",
        "self-doubt": "[*] You belong here. Your achievements are real - own your success!",
        "general": "[*] Every challenge carries the seed of opportunity. You've got this!",
        "emergency": "[URGENT] You matter deeply. Please reach out for immediate help:\n\n[CALL] National Crisis Line: 988 (US)\n[WEB] International Association for Suicide Prevention: https://www.iasp.info/resources/Crisis_Centres/\n\nPlease talk to someone you trust or a mental health professional right away."
    }

    return messages.get(stress_type, messages["general"])


def run_interactive():
    """
    Run the interactive CLI mode - takes user input and displays recommendations
    """
    print("=" * 60)
    print("[APP] OpenAlex Book Recommendation System")
    print("=" * 60)
    print("\nEnter your concern or stress type to get book recommendations!")
    print("Type 'quit' or 'exit' to end the program.\n")

    while True:
        # Get user input
        user_input = input("[USER] You: ").strip()

        if not user_input:
            print("Please enter something...\n")
            continue

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\n[BYE] Thank you for using the recommendation system. Take care!")
            break

        # Classify the stress type
        stress_type = classify_stress(user_input)
        print(f"\n[DETECT] Detected stress type: {stress_type.upper()}")

        # Handle emergency case
        if stress_type == "emergency":
            print("\n" + "=" * 40)
            print(get_motivation("emergency"))
            print("=" * 40)
            print("\nPlease seek immediate help. Would you like book recommendations anyway? (y/n): ")
            continue_choice = input("> ").strip().lower()
            if continue_choice != 'y':
                continue

        # Get motivation
        print("\n[SUPPORT] Motivation:")
        print(get_motivation(stress_type))

        # Get book recommendations
        print(f"\n[SEARCH] Searching for books related to {stress_type}...")
        recommendations = get_book_recommendations(stress_type, limit=3)

        if recommendations:
            print("\n" + "=" * 60)
            print("[RESULTS] RECOMMENDED BOOKS")
            print("=" * 60)

            for i, book in enumerate(recommendations, 1):
                print(f"\n--- Book {i} ---")
                print(f"[TITLE] Title: {book['title']}")
                print(f"[AUTH] Author(s): {book['author']}")
                print(f"[DATE] Year: {book['year']}")
                print(f"[PUBL] Publisher: {book['publisher'] or 'N/A'}")
                print(f"[DOI] DOI: {book['doi'] or 'N/A'}")
                print(f"[CITE] Cited by: {book['cited_by_count']} scholarly works")
                print(f"[AVAIL] Availability: {book['availability']}")
        else:
            print("\n[NONE] No books found for this category. Please try a different description.")

        print("\n" + "=" * 60)
        print("Would you like to search for another concern? (y/n)")
        continue_choice = input("> ").strip().lower()

        if continue_choice != 'y':
            print("\n[BYE] Thank you for using the recommendation system. Take care!")
            break


# Test the module
if __name__ == "__main__":
    import sys
    
    # Check if running with command line arguments
    if len(sys.argv) > 1:
        # If arguments provided, use them
        stress_type = sys.argv[1]
        print(f"Searching for books related to: {stress_type}")
        books = get_book_recommendations(stress_type, limit=3)
        
        for i, book in enumerate(books, 1):
            print(f"\n--- Book {i} ---")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
            print(f"Publisher: {book['publisher']}")
            print(f"Open Access: {book['availability']}")
            print(f"Cited by: {book['cited_by_count']}")
    else:
        # Run interactive mode if no arguments provided
        run_interactive()
        