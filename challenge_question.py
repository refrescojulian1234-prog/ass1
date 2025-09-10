# Maths Test Program - Challenge Question
# Added challenge question functionality. 

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
    print("Test your addition and subtraction.")
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
            print("Incorrect choice. Please try again.")

    print(f"This test will have {questions} questions.")
    print()
    
    # Test administration
    score = 0
    correct_answers = []
    response_times = []
    
    for i in range(1, questions + 1):
        print(f"Score: {score} | Question {i} of {questions}")
        
        # Determine question range
        if i == questions:  # Challenge question
            print("Challenge question!")
            min_range = max_num
            max_range = max_num * 2
        else:
            min_range = 1
            max_range = max_num
        
        # Generate and ask question
        question = create_question(min_range, max_range)
        is_correct, time_taken = ask_question(question)
        
        # Score calculation
        if is_correct:
            points = max(1, 10 - time_taken)
            score += points
            print(f"Correct! +{points} points ({time_taken}s)")
        else:
            print(f"Incorrect! 0 points ({time_taken}s)")
        
        # Store results
        correct_answers.append(is_correct)
        response_times.append(time_taken)
        print()
    
    # Calculate results
    correct_count = sum(correct_answers)
    correct_percentage = round((correct_count / questions) * 100)
    avg_response_time = round(sum(response_times) / questions)
    
    # Display results
    print("=" * 40)
    print("TEST RESULTS")
    print("=" * 40)
    print(f"Final Score: {score}")
    print(f"Correct Answers: {correct_count}/{questions} ({correct_percentage}%)")
    print(f"Average Response Time: {avg_response_time} seconds")

if __name__ == "__main__":
    main()