"""
Keyword Extraction Module for MindEase
Extracts relevant keywords from user input for better analysis
"""

import re
from collections import Counter


# Common English stop words
STOP_WORDS = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your',
    'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she',
    'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their',
    'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'why', 'how',
    'all', 'each', 'every', 'both', 'few', 'more', 'most', 'other', 'some',
    'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
    'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'a', 'an',
    'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 'have',
    'in', 'is', 'it', 'its', 'of', 'on', 'or', 'the', 'to', 'was', 'were', 'am',
    'is', 'been', 'being', 'having', 'doing', 'did', 'does', 'would', 'could',
    'ought', 'i\'m', 'you\'re', 'he\'s', 'she\'s', 'it\'s', 'we\'re', 'they\'re',
    'i\'ve', 'you\'ve', 'we\'ve', 'they\'ve', 'i\'d', 'you\'d', 'he\'d', 'she\'d',
    'we\'d', 'they\'d', 'i\'ll', 'you\'ll', 'he\'ll', 'she\'ll', 'we\'ll', 'they\'ll',
    'isn\'t', 'aren\'t', 'wasn\'t', 'weren\'t', 'hasn\'t', 'haven\'t', 'hadn\'t',
    'doesn\'t', 'don\'t', 'didn\'t', 'won\'t', 'wouldn\'t', 'shan\'t', 'shouldn\'t',
    'can\'t', 'cannot', 'couldn\'t', 'mustn\'t', 'let\'s', 'that\'s', 'who\'s',
    'what\'s', 'here\'s', 'there\'s', 'when\'s', 'where\'s', 'why\'s', 'how\'s'
}


def extract_keywords(text, max_keywords=10):
    """
    Extract keywords from text.
    
    Args:
        text: Input text string
        max_keywords: Maximum number of keywords to extract
        
    Returns:
        List of extracted keywords
    """
    # Convert to lowercase
    text_lower = text.lower()
    
    # Remove special characters but keep spaces
    text_clean = re.sub(r'[^\w\s]', '', text_lower)
    
    # Split into words
    words = text_clean.split()
    
    # Filter out stop words and short words
    keywords = [
        word for word in words 
        if word not in STOP_WORDS and len(word) > 2
    ]
    
    # Get most frequent keywords
    if keywords:
        counter = Counter(keywords)
        top_keywords = [word for word, count in counter.most_common(max_keywords)]
        return top_keywords
    
    return []


def extract_phrases(text, min_phrase_length=2):
    """
    Extract meaningful phrases from text.
    
    Args:
        text: Input text string
        min_phrase_length: Minimum length of phrase (in words)
        
    Returns:
        List of extracted phrases
    """
    text_lower = text.lower()
    
    # Split by common separators
    sentences = re.split(r'[.!?;]', text_lower)
    
    phrases = []
    for sentence in sentences:
        # Remove extra spaces and split
        words = sentence.strip().split()
        
        # Filter stop words
        filtered_words = [
            word.strip(',') for word in words 
            if word.strip(',') not in STOP_WORDS and len(word.strip(',')) > 2
        ]
        
        # Create phrases of min length
        if len(filtered_words) >= min_phrase_length:
            phrase = ' '.join(filtered_words)
            if len(phrase) > 5:  # Ensure meaningful length
                phrases.append(phrase)
    
    return phrases[:5]  # Return top 5 phrases


def get_keyword_sentiment(keywords):
    """
    Analyze sentiment of keywords to determine emotional state.
    
    Args:
        keywords: List of keywords
        
    Returns:
        Dictionary with sentiment analysis
    """
    positive_words = {
        'happy', 'good', 'great', 'love', 'awesome', 'excellent', 'wonderful',
        'fantastic', 'amazing', 'beautiful', 'confident', 'strong', 'capable',
        'motivated', 'hopeful', 'peaceful', 'calm', 'content'
    }
    
    negative_words = {
        'sad', 'bad', 'terrible', 'hate', 'awful', 'horrible', 'depressed',
        'anxious', 'worried', 'stressed', 'overwhelmed', 'tired', 'exhausted',
        'lonely', 'scared', 'afraid', 'panic', 'angry', 'frustrated', 'helpless',
        'hopeless', 'useless', 'failure', 'broken'
    }
    
    neutral_words = {
        'think', 'feel', 'change', 'problem', 'difficult', 'hard', 'challenge',
        'struggle', 'issue', 'concern', 'matter'
    }
    
    keyword_set = set(keywords)
    
    positive_count = len(keyword_set & positive_words)
    negative_count = len(keyword_set & negative_words)
    neutral_count = len(keyword_set & neutral_words)
    
    total = positive_count + negative_count + neutral_count
    
    if total == 0:
        sentiment = "neutral"
        intensity = "moderate"
    else:
        if negative_count > positive_count:
            sentiment = "negative"
            intensity = "high" if negative_count >= 3 else "moderate"
        elif positive_count > negative_count:
            sentiment = "positive"
            intensity = "high" if positive_count >= 3 else "moderate"
        else:
            sentiment = "neutral"
            intensity = "moderate"
    
    return {
        "sentiment": sentiment,
        "intensity": intensity,
        "positive_keywords": list(keyword_set & positive_words),
        "negative_keywords": list(keyword_set & negative_words),
        "neutral_keywords": list(keyword_set & neutral_words)
    }


# Test
if __name__ == "__main__":
    test_text = "I'm feeling really anxious and overwhelmed about my upcoming exam. I have so much to study and I don't think I can handle it all."
    
    print("Original Text:")
    print(test_text)
    print("\nExtracted Keywords:")
    keywords = extract_keywords(test_text)
    print(keywords)
    
    print("\nExtracted Phrases:")
    phrases = extract_phrases(test_text)
    for phrase in phrases:
        print(f"  - {phrase}")
    
    print("\nSentiment Analysis:")
    sentiment = get_keyword_sentiment(keywords)
    print(f"  Sentiment: {sentiment['sentiment']}")
    print(f"  Intensity: {sentiment['intensity']}")
    print(f"  Negative Keywords: {sentiment['negative_keywords']}")
