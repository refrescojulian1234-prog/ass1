# Maths Test Program - Question Functions
# Added create_question and ask_question functions. 

import random
import time

def create_question(min_num, max_num):
    """Create a random maths question"""
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)
    operator = random.choice(['+', '-'])
    return f"{num1} {operator} {num2}"

def ask_question(question):
    """Ask a question and record response time"""
    start_time = time.time()
    user_answer = int(input(f"{question} = "))
    end_time = time.time()
    
    time_taken = int(end_time - start_time)
    correct_answer = eval(question)
    is_correct = user_answer == correct_answer
    
    return (is_correct, time_taken)

def main():
    print("Welcome to Julian's Maths Test Program!")
    print("Test your addition and subtraction skills.")
    print()
    
    # Difficulty selection
    difficulties = {
        '1': ('Easy', 5, 10),
        '2': ('Medium', 10, 20),
        '3': ('Hard', 15, 50)
    }
    
    while True:
        choice = input("Choose difficulty (1-Easy, 2-Medium, 3-Hard): ")
        if choice in difficulties:
            difficulty, questions, max_num = difficulties[choice]
            print(f"You selected {difficulty} difficulty.")
            break
        else:
            print("Invalid choice. Please try again.")
    
    print(f"The test will have {questions} questions.")
    print()
    
    # Test administration
    score = 0
    for i in range(1, questions + 1):
        print(f"Score: {score} | Question {i} of {questions}")
        print("      ")       
        # Generate and ask question
        question = create_question(1, max_num)
        is_correct, time_taken = ask_question(question)
        
        # Score calculation
        if is_correct:
            points = max(1, 10 - time_taken)
            score += points
            print(f"Correct! +{points} points ({time_taken}s)")
        else:
            print(f"Incorrect! 0 points ({time_taken}s)")
        
        print()
    
    print(f"Final Score: {score}")

if __name__ == "__main__":
    main()