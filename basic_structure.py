# Maths Test Program - Basic Structure for the code 
# Added difficulty selection and basic question generation 

import random

def main():
    print("Welcome to Julian's Maths Test Program!")
    print("Test your addition and subtraction.")
    print()
    
    # Difficulty selection placeholder
    print("Difficulty levels: 1-Easy, 2-Medium, 3-Hard")
    difficulty = input("Choose difficulty: ")
    
    # Basic question generation test
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-'])
    
    question = f"{num1} {operator} {num2}"
    print(f"Sample question: {question} = ?")

if __name__ == "__main__":
    main()