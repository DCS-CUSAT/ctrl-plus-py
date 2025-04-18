import json

def load_quiz(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def run_quiz(quiz_data):
    score = 0
    for question, details in quiz_data.items():
        print("\n" + question)
        for option in details["options"]:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").upper()
        
        if user_answer == details["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {details['answer']}.")

    print(f"\n🎉 Quiz completed! Your final score is {score}/{len(quiz_data)}")

# Main
quiz_data = load_quiz("question.json")
run_quiz(quiz_data)
