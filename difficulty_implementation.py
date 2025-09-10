# Maths Test Program - Difficulty Implementation   
# Added proper difficulty handling and question count

import random

def main():
    print("Welcome to Julian's Maths Test Program!")
    print("Test your addition and subtraction.")
    print()
    
    # Difficulty selection with validation
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
    
    # Test loop structure
    score = 0
    for i in range(1, questions + 1):
        print(f"Question {i} of {questions}")
        
        # Generate question
        num1 = random.randint(1, max_num)
        num2 = random.randint(1, max_num)
        operator = random.choice(['+', '-'])
        
        question = f"{num1} {operator} {num2}"
        print(f"{question} = ?")
        
        # Placeholder for asking question
        print("(Question asking functionality to be implemented)")
        print()

if __name__ == "__main__":
    main()