# Quiz questions list
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "Who is known as the Father of the Nation in India?",
        "options": ["Mahatma Gandhi", "Jawaharlal Nehru", "B. R. Ambedkar", "Subhash Chandra Bose"],
        "answer": "Mahatma Gandhi"
    },
    {
        "question": "Which animal is called the King of the Jungle?",
        "options": ["Tiger", "Lion", "Elephant", "Leopard"],
        "answer": "Lion"
    },
    {
        "question": "What is the national sport of India?",
        "options": ["Cricket", "Hockey", "Football", "Kabaddi"],
        "answer": "Hockey"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Which festival is known as the Festival of Lights?",
        "options": ["Diwali", "Holi", "Eid", "Christmas"],
        "answer": "Diwali"
    },
    {
        "question": "Which gas do humans need to breathe?",
        "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"],
        "answer": "Oxygen"
    },
    {
        "question": "Which is the fastest land animal?",
        "options": ["Cheetah", "Horse", "Tiger", "Leopard"],
        "answer": "Cheetah"
    }
]

score = 0  # start with score 0

# Loop through each question
for q in questions:
    print(q["question"])  # print the question
    for i, option in enumerate(q["options"], start=1):
        print(f"{i}. {option}")  # print options
    
    # take user input
    choice = int(input("Choose your answer (1-4): "))
    user_answer = q["options"][choice - 1]  # selected option
    
    # print the chosen answer
    print(f"You selected: {user_answer}")
    
    # check correct/incorrect
    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong!\n")

# final score
print(f"Your total score is: {score}/{len(questions)}")
