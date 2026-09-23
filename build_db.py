import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from create_db import create_database, verify_database

if __name__ == "__main__":
    print("=" * 60)
    print("[BUILD] Building MindEase Library Database")
    print("=" * 60)
    create_database()
    print()
    verify_database()
    print("\n[DONE] Database setup complete!")
