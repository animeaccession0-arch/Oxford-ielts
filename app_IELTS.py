# =====================================
# IELTS 7.5 MASTER PREP SYSTEM
# Security + API Key + All 4 Sections
# =====================================

import os
import datetime
from dotenv import load_dotenv

# ========== 1. SECURITY CONFIG ==========
PASSWORD = "OxfordCS@2027" # CHANGE THIS PASSWORD
MAX_ATTEMPTS = 3

def login():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        attempt = input("Enter Password to Access IELTS Repo: ")
        if attempt == PASSWORD:
            print("Login Successful ✅\n")
            return True
        else:
            attempts += 1
            print(f"Wrong Password! {MAX_ATTEMPTS - attempts} attempts left")
    print("Access Denied. Exiting.")
    exit()

# ========== 2. API KEY LOADER ==========
def load_api_key():
    load_dotenv() # Loads from.env file
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Warning: API_KEY not found in.env file")
        print("Create a.env file with: API_KEY=your_key_here")
    else:
        print("API Key Loaded ✅")
    return api_key

# ========== 3. STUDY PLAN ==========
def show_study_plan():
    print("\n--- 60 DAY IELTS 7.5 PLAN ---")
    plan = {
        "Week 1-2: Foundation": "Listening 1 Section, Reading 1 Passage, Writing Task1, Speaking 5 Qs daily",
        "Week 3-4: Practice": "2 Full Tests per week, 2 Essays per week, Record Speaking",
        "Week 5-6: Mock Exams": "1 Full Mock per week + Error Log Review"
    }
    for week, task in plan.items():
        print(f"{week}: {task}")

# ========== 4. LISTENING TRACKER ==========
score_log = []
def add_listening_score():
    try:
        score = int(input("Enter Listening Score out of 40: "))
        if 0 <= score <= 40:
            score_log.append(score)
            band = round((score / 40) * 9, 1)
            print(f"Test {len(score_log)}: {score}/40 | Estimated Band: {band}")
            print("Target for Oxford: 30+ for Band 7.5")
        else:
            print("Score must be between 0 and 40")
    except ValueError:
        print("Please enter a number")

# ========== 5. READING TIPS ==========
def reading_tips():
    print("\n--- READING SECTION TIPS ---")
    tips = [
        "1. Time Management: 20 minutes per passage",
        "2. Scan for Keywords before reading full passage",
        "3. T/F/NG Rule: Not in text = NG, Wrong info = False",
        "4. Practice with Cambridge IELTS 10-18"
    ]
    for tip in tips: print(tip)

# ========== 6. WRITING TEMPLATES ==========
def writing_helper():
    print("\n--- WRITING TASK 2 TEMPLATE ---")
    topic = input("Enter Essay Topic: ")
    template = f"""
    Introduction: It is a common belief that {topic}.
    While some argue that [View 1], I firmly believe that [View 2].

    Body Paragraph 1: To begin with, [Point 1].
    For example, [Specific Example].

    Body Paragraph 2: Furthermore, [Point 2].
    This is because [Reason/Explanation].

    Conclusion: In conclusion, [Summarize].
    Therefore, [Final Opinion].

    Target: 260+ words, 4 Paragraphs
    """
    print(template)
    print("\nSend me your essay and I will check your Band score")

# ========== 7. SPEAKING QUESTIONS ==========
def speaking_practice():
    print("\n--- SPEAKING QUESTIONS ---")
    part1 = ["Describe your hometown Mumbai", "Do you enjoy coding?", "What do you do in free time?"]
    part2 = ["Describe an app you developed", "Describe a teacher who influenced you"]
    part3 = ["How will AI change education?", "Is coding essential for the future?"]

    print("Part 1 - 5 min:", part1)
    print("Part 2 - Cue Card 2 min:", part2)
    print("Part 3 - Discussion 4 min:", part3)
    print("Tip: Record yourself and listen back")

# ========== 8. SAVE PROGRESS ==========
def save_progress():
    today = datetime.date.today()
    with open("progress.txt", "a") as f:
        f.write(f"{today}: Tests Completed = {len(score_log)}, Last Score = {score_log[-1] if score_log else 'N/A'}\n")
    print("Progress Saved to progress.txt ✅")

# ========== MAIN DASHBOARD ==========
def main():
    login()
    api_key = load_api_key()

    while True:
        print("\n========== IELTS DASHBOARD ==========")
        print("1. Study Plan 2. Add Listening Score 3. Reading Tips")
        print("4. Writing Template 5. Speaking Practice 6. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == "1": show_study_plan()
        elif choice == "2": add_listening_score()
        elif choice == "3": reading_tips()
        elif choice == "4": writing_helper()
        elif choice == "5": speaking_practice()
        elif choice == "6": save_progress(); print("Goodbye!"); break
        else: print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
