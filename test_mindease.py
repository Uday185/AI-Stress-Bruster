# -*- coding: utf-8 -*-
"""
Quick test script to verify MindEase installation and functionality
"""

import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("\n" + "=" * 70)
print("[TEST] MindEase System Test")
print("=" * 70 + "\n")

# Test 1: Check database
print("[*] Test 1: Checking database...")
if os.path.exists("library.db"):
    import sqlite3
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM books")
    count = cursor.fetchone()[0]
    print(f"  [OK] Database found with {count} books\n")
    conn.close()
else:
    print("  [FAIL] Database not found\n")

# Test 2: Check keyword extractor
print("[*] Test 2: Testing keyword extractor...")
try:
    from keyword_extractor import extract_keywords, extract_phrases, get_keyword_sentiment
    test_text = "I'm feeling anxious and overwhelmed about my exam coming up"
    keywords = extract_keywords(test_text)
    phrases = extract_phrases(test_text)
    sentiment = get_keyword_sentiment(keywords)
    print(f"  [OK] Keywords extracted: {keywords}")
    print(f"  [OK] Sentiment: {sentiment['sentiment']} ({sentiment['intensity']})\n")
except Exception as e:
    print(f"  [FAIL] Error: {e}\n")

# Test 3: Check stress classification
print("[*] Test 3: Testing stress classification...")
try:
    from app import classify_stress

    test_cases = [
        ("I have an exam tomorrow", "academic"),
        ("I'm feeling really sad and empty", "emotional"),
        ("My boss is stressing me out", "career"),
        ("I'm worried about money", "financial"),
    ]

    for text, expected in test_cases:
        result = classify_stress(text)
        status = "[OK]" if result == expected else f"[WARN] (got {result})"
        print(f"  {status} '{text[:40]}...' -> {result}")
    print()
except Exception as e:
    print(f"  [FAIL] Error: {e}\n")

# Test 4: Check Flask
print("[*] Test 4: Checking Flask...")
try:
    import flask
    try:
        from importlib.metadata import version
        flask_version = version("flask")
    except:
        flask_version = flask.__version__
    print(f"  [OK] Flask {flask_version} installed\n")
except Exception as e:
    print(f"  [FAIL] Flask not found: {e}\n")

print("=" * 70)
print("[DONE] All tests completed!")
print("=" * 70)
print("\n[RUN] To start the web app, run: python app.py\n")
