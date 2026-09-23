# 🧠💙 MindEase - Stress Relief & Book Recommendation System

**MindEase** is an AI-powered web application that analyzes user concerns, identifies stress types, extracts keywords from sentences, and recommends philosophical and ethical books for mental wellness and stress relief.

---

## 📋 Features

✅ **AI Stress Analysis** - Classifies 17+ different types of stress and emotional challenges
✅ **Keyword Extraction** - Identifies and highlights key themes in user input
✅ **Sentiment Analysis** - Analyzes emotional intensity and sentiment
✅ **Personalized Recommendations** - Suggests curated philosophical and ethical books
✅ **Motivational Support** - Provides uplifting, compassionate messages
✅ **Beautiful UI** - Modern, responsive web interface
✅ **Local Database** - 51 carefully curated books covering all stress categories
✅ **Emergency Support** - Crisis resources for urgent situations

---

## 🎯 Supported Stress Categories

1. **Academic** - Exam anxiety, study stress, college pressure
2. **Anxiety** - Panic, overthinking, worry, nervousness
3. **Emotional** - Depression, sadness, grief, emotional struggles
4. **Career** - Job stress, promotion pressure, career change
5. **Financial** - Money worries, debt, budgeting stress
6. **Family** - Family conflict, parenting stress, household issues
7. **Confidence** - Self-doubt, insecurity, shyness
8. **Social** - Social anxiety, meeting people, conversation issues
9. **Loneliness** - Isolation, disconnection, lack of friends
10. **Breakup** - Heartbreak, relationship loss, divorce recovery
11. **Health** - Medical stress, illness, health anxiety
12. **Peer Pressure** - Social influence, bullying, fitting in
13. **Relationship** - Romantic relationship issues, communication problems
14. **Self-Esteem** - Worthlessness feelings, self-worth issues
15. **Time Management** - Procrastination, deadline pressure, busyness
16. **Self-Doubt** - Impostor syndrome, perfectionism, inadequacy
17. **General** - General well-being and resilience

---

## 📚 Book Database

The system includes **51 curated books** across all stress categories:
- **Philosophical works** (Marx Aurelius, Plato, Albert Camus, etc.)
- **Ethical guides** (ethics of care, virtue ethics, authentic living)
- **Psychology** (emotional intelligence, mindfulness, attachment theory)
- **Self-help** (practical strategies and personal development)
- **Wellness** (stress management, meditation, healing)

Each book entry includes:
- Title and Author
- Chapter/Section reference  
- Summary and description
- Shelf category (Philosophy, Psychology, Self-Help, etc.)
- Availability status
- Priority level

### Example Books Included:
- "Man's Search for Meaning" - Viktor Frankl
- "The Consolations of Philosophy" - Alain de Botton
- "Emotional Intelligence" - Daniel Goleman
- "Atomic Habits" - James Clear
- "Nonviolent Communication" - Marshall B. Rosenberg
- "Meditations" - Marcus Aurelius
- And 45 more...

---

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Flask
- Virtual environment (recommended)

### Setup Steps

1. **Navigate to project directory:**
```bash
cd "C:\Users\Dinesha\Desktop\semester project"
```

2. **Activate virtual environment:**
```bash
.\.venv\Scripts\Activate.ps1
```

3. **Navigate to app directory:**
```bash
cd "semester project"
```

4. **Initialize the database:**
```bash
python create_db.py
```
This creates `library.db` with 51 books across 17 categories.

5. **Run the Flask app:**
```bash
python app.py
```

6. **Access the web app:**
Open your browser and go to `http://localhost:5000`

---

## 🚀 Usage

1. **Open MindEase** at http://localhost:5000
2. **Share your concern** - Write what's on your mind in the textarea
3. **Get Analysis** - Click "Get Support & Book Recommendations"
4. **View Results**:
   - 🔍 Keywords extracted from your message
   - 💭 Emotional sentiment analysis
   - 📚 Personalized book recommendation
   - 💬 Supportive motivational message
   - 📊 Category classification

### Example Input:
> "I'm feeling really anxious and overwhelmed about my upcoming exam. I have so much to study and I don't think I can handle it all."

### Example Output:
- **Stress Type**: Academic
- **Keywords**: anxious, overwhelmed, exam, study, pressure
- **Sentiment**: Negative (High intensity)
- **Recommended Book**: "The Art of Learning" by Josh Waitzkin
- **Message**: Motivational support tailored to academic stress

---

## 🔍 Keyword Extraction Features

### What It Does:
- Extracts meaningful keywords from user input
- Filters out common stop words
- Identifies emotional sentiment
- Analyzes intensity of emotions

### Example:
```
Input: "I'm struggling with my boss and feeling really stressed at work"
Keywords: ['struggling', 'boss', 'stressed', 'work']
Sentiment: Negative (Moderate Intensity)
Negative Keywords: ['stressed', 'struggling']
Classification: Career Stress
```

---

## 📁 Project Structure

```
semester project/
├── app.py                    # Main Flask application
├── keyword_extractor.py      # Keyword extraction module
├── create_db.py             # Database creation script
├── test_mindease.py         # System test script
├── library.db               # SQLite database (created on first run)
├── requirements.txt         # Python dependencies
│
├── templates/
│   ├── index.html          # Home page
│   ├── result.html         # Results page
│   └── error.html          # Error page
│
└── .venv/                  # Python virtual environment
```

---

## 📖 Module Descriptions

### `app.py`
Main Flask application that handles:
- Stress classification
- Route handling
- Database queries
- Session management

### `keyword_extractor.py`
Keyword and sentiment analysis:
- Extracts keywords from text
- Removes stop words
- Analyzes emotional sentiment
- Identifies phrase patterns

### `create_db.py`
Database initialization:
- Creates `library.db`
- Populates with 51 books
- Organizes by stress category
- Validates structure

### `test_mindease.py`
System validation:
- Tests database connectivity
- Validates keyword extraction
- Tests stress classification
- Verifies Flask installation

---

## 🎨 Web Interface

### Home Page (`index.html`)
- Beautiful gradient background
- Input textarea for user concerns
- Feature highlights
- Disclaimer about professional help

### Results Page (`result.html`)
- Stress type badge
- Extracted keywords display
- Sentiment analysis
- Book recommendation card
- Motivational message
- Beautiful typography and spacing

### Error Page (`error.html`)
- User-friendly error messages
- Navigation back to home

---

## 🧪 Testing

Run the test script to verify installation:

```bash
python test_mindease.py
```

This validates:
✅ Database connectivity
✅ Keyword extraction functionality
✅ Stress classification accuracy
✅ Flask installation
✅ All system components

---

## 💡 How Stress Classification Works

The system uses multi-level classification:

1. **Emergency Detection** - Identifies crisis indicators first (highest priority)
2. **Specific Category Match** - Matches keywords to stress categories
3. **Keyword Analysis** - Uses extracted keywords for enhanced classification
4. **Sentiment Context** - Considers emotional tone
5. **Fallback to General** - Returns "general" if no specific match

### Priority Order:
1. Emergency → Career → Financial → Academic → Anxiety → Emotional → etc.

---

## 🤝 Recommendation Algorithm

1. **Load books** from database for classified stress type
2. **Filter available** books
3. **Sort by priority** (lower number = higher priority)
4. **Select randomly** from top priority books for variety
5. **Return with metadata** (title, author, chapter, summary)

This ensures different recommendations on subsequent visits.

---

## 📞 Crisis Resources

If you or someone you know is in crisis:

🇺🇸 **United States:**
- National Suicide Prevention Lifeline: **988**
- Crisis Text Line: Text **HOME** to **741741**
- International Association for Suicide Prevention: https://www.iasp.info/resources/Crisis_Centres/

---

## ⚠️ Important Disclaimer

**MindEase is NOT a substitute for professional mental health care.**

- Not a diagnostic tool
- Not a replacement for therapy
- Not a crisis intervention service
- Should not be used for self-diagnosis

If you're experiencing a crisis or severe mental health issues, please:
- Call emergency services
- Contact a mental health professional
- Reach out to a crisis helpline
- Go to the nearest emergency room

---

## 🎓 Educational Use

When sharing what's on your mind, you can mention:
- Academic stress (exams, assignments, grades)
- Personal challenges (relationships, family, self-esteem)
- External pressures (career, finances, peers)
- Emotional wellbeing (depression, anxiety, loneliness)

MindEase will analyze and categorize your concerns appropriately.

---

## 🔧 Troubleshooting

### Database Not Found
```bash
# Recreate the database
python create_db.py
```

### Flask Not Starting
```bash
# Ensure virtual environment is activated
.\.venv\Scripts\Activate.ps1

# Install Flask if needed
pip install flask
```

### Port 5000 Already in Use
```bash
# Use different port - edit app.py:
app.run(debug=True, port=5001)
```

### Keywords Not Extracting
- Ensure `keyword_extractor.py` is in same directory as `app.py`
- Check that imports are working with `test_mindease.py`

---

## 📊 System Statistics

- **Stress Categories**: 17
- **Books in Database**: 51
- **Books per Category**: 3 (minimum)
- **Keyword Stop Words**: 100+
- **Classification Keywords**: 300+
- **Response Time**: <100ms average
- **Database Size**: ~50KB

---

## 🌟 Features Roadmap

Potential future enhancements:
- User profiles and history
- Multiple language support
- Mobile app version
- Integration with mental health resources
- AI-powered chatbot support
- Personalized recommendation engine
- User feedback system
- Integration with libraries for actual book access

---

## 📝 License

This project is created for educational purposes to support mental wellness and stress relief.

---

## 👨‍💻 Development

**Created**: April 2026
**Version**: 1.0
**Status**: Fully Functional

---

## 📧 Support

For issues or questions about MindEase:
1. Check this README
2. Run `test_mindease.py` to validate installation
3. Review the error messages in the web interface
4. Check Flask debug output in terminal

---

## 🙏 Acknowledgments

This project combines:
- Philosophical wisdom from classic and modern authors
- Psychological insights from research-backed practices
- Ethical approaches to mental wellness
- Educational best practices for stress management

---

**Remember: You are not alone. Help is available. MindEase is here to support you. 💙**

---

## Quick Start Guide

```bash
# 1. Navigate to project
cd "C:\Users\Dinesha\Desktop\semester project\semester project"

# 2. Activate environment
..\. .venv\Scripts\Activate.ps1

# 3. Create database
python create_db.py

# 4. Start server
python app.py

# 5. Open browser
# Visit http://localhost:5000
```

Enjoy using MindEase! 🌟
