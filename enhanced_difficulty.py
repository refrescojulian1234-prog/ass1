# Maths Test Program - Enhanced Difficulty. 
# Added enhanced difficulty options and input validation. 

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
    try:
        user_answer = int(input(f"{question} = "))
    except ValueError:
        user_answer = None
    end_time = time.time()
    
    time_taken = int(end_time - start_time)
    
    try:
        correct_answer = eval(question)
        is_correct = user_answer == correct_answer
    except:
        is_correct = False
        
    return (is_correct, time_taken)

def main():
    print("Welcome to Maths Test Program!")
    print("Test your addition and subtraction skills.")
    print()
    
    # Enhanced difficulty selection
    difficulties = {
        '1': ('easy', 5, 10),
        'e': ('easy', 5, 10),
        'easy': ('easy', 5, 10),
        '2': ('medium', 10, 20),
        'm': ('medium', 10, 20),
        'medium': ('medium', 10, 20),
        '3': ('hard', 15, 50),
        'h': ('hard', 15, 50),
        'hard': ('hard', 15, 50)
    }
    
    while True:
        choice = input("Choose difficulty (1-Easy, 2-Medium, 3-Hard): ").lower().strip()
        if choice in difficulties:
            difficulty, questions, max_num = difficulties[choice]
            print(f"You selected {difficulty.capitalize()} difficulty.")
            break
        else:
            print("Invalid choice. Please try again.")
    
    print(f"The test will have {questions} questions.")
    print()
    
    # Test administration
    score = 0
    correct_answers = []
    response_times = []
    questions_list = []
    
    for i in range(1, questions + 1):
        print(f"Score: {score} | Question {i} of {questions}")
        
        # Determine question range
        if i == questions:  # Challenge question
            print("Challenge question!")
            min_range = max_num
            max_range = max_num * 2
        else:
            min_range = max_num // 2
            max_range = max_num
        
        # Generate and ask question
        question = create_question(min_range, max_range)
        questions_list.append(question)
        is_correct, time_taken = ask_question(question)
        
        # Score calculation with proper pluralization
        if is_correct:
            points = max(1, 10 - time_taken)
            score += points
            point_text = "point" if points == 1 else "points"
            second_text = "second" if time_taken == 1 else "seconds"
            print(f"Correct! You took {time_taken} {second_text} and earned {points} {point_text}.")
        else:
            second_text = "second" if time_taken == 1 else "seconds"
            print(f"Incorrect! You took {time_taken} {second_text} and earned 0 points.")
        
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
    print()
    
    # Question breakdown
    print("Question Breakdown:")
    print("-" * 40)
    print(f"{'Question':<10} {'Correct':<8} {'Time':>8}")
    print("-" * 40)
    for i, (correct, time_taken) in enumerate(zip(correct_answers, response_times), 1):
        status = "YES" if correct else "NO"
        print(f"Q{i:<9} {status:<8} {time_taken:>7}s")
    print("-" * 40)

if __name__ == "__main__":
    main()