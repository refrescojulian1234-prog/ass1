# Julian's Math Test Program

**Author:** Julian Mendis  
**Student Number:** 10685665  
**Date:** 10/09/2025

A Python-based interactive math quiz program that tests users' addition and subtraction skills with multiple difficulty levels and performance tracking.

## 🎯 Features

- **Multiple Difficulty Levels**: Easy, Medium, and Hard with varying question counts and number ranges
- **Flexible Input**: Accepts numerical input (1, 2, 3) or text input (easy, medium, hard, e, m, h)
- **Challenge Question**: Final question with increased difficulty for bonus points
- **Performance Tracking**: Records response times and calculates scores based on speed and accuracy
- **Detailed Results**: Comprehensive breakdown of performance with question-by-question analysis
- **Error Handling**: Graceful handling of invalid inputs and non-numerical responses

## 📂 Project Structure

### Main Branch
- **`az.py`** - Complete, production-ready version of the math test program

### Development Branch
- **`initial_design.py`** - Initial program concept and outline
- **`basic_structure.py`** - Basic program structure with difficulty selection
- **`difficulty_implementation.py`** - Implementation of difficulty levels and question counting
- **`question_functions.py`** - Core question generation and asking functions
- **`challenge_question.py`** - Addition of challenge question functionality
- **`enhanced_difficulty.py`** - Enhanced difficulty options and input validation

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- No additional libraries required (uses built-in modules: `time`, `random`)

### Running the Program
```bash
python az.py
```

## 🎮 How to Play

1. **Welcome Screen**: The program displays a welcome message and instructions
2. **Difficulty Selection**: Choose from:
   - **Easy**: 5 questions, numbers 5-10, challenge question 10-20
   - **Medium**: 10 questions, numbers 10-20, challenge question 20-40
   - **Hard**: 15 questions, numbers 15-50, challenge question 50-100
3. **Answer Questions**: Solve addition and subtraction problems as quickly as possible
4. **Scoring**: Earn points based on correctness and speed (max 10 points per question)
5. **Results**: View detailed performance statistics and question breakdown

## 📊 Scoring System

- **Correct Answer**: Base score of 10 points minus response time in seconds (minimum 1 point)
- **Incorrect Answer**: 0 points
- **Speed Bonus**: Faster responses earn more points
- **Challenge Question**: Same scoring rules apply with higher difficulty numbers

## 🔧 Technical Details

### Key Functions
- `create_question(min_num, max_num)`: Generates random math questions within specified range
- `ask_question(question)`: Handles user input, timing, and correctness validation
- `main()`: Controls program flow and user interface

### Difficulty Configuration
| Level | Questions | Number Range | Challenge Range |
|-------|-----------|-------------|----------------|
| Easy | 5 | 5-10 | 10-20 |
| Medium | 10 | 10-20 | 20-40 |
| Hard | 15 | 15-50 | 50-100 |

## 📈 Development Timeline

The project evolved through several iterations:

1. **Initial Design** - Basic concept and program outline
2. **Basic Structure** - Welcome message and difficulty selection framework
3. **Difficulty Implementation** - Working difficulty levels with question counts
4. **Question Functions** - Core question generation and user interaction
5. **Challenge Question** - Special final question with increased difficulty
6. **Enhanced Difficulty** - Multiple input formats and improved validation
7. **Final Version (az.py)** - Polished interface with comprehensive error handling

## 🎨 Sample Output

```
________________________________________________________

Welcome to Julian's Maths Test Program !
Test your addition and subtraction.
________________________________________________________

Choose difficulty (1-Easy, 2-Medium, 3-Hard): 1
You have selected Easy difficulty.
This test will have 5 questions.

Score: 0 | Question 1 of 5
 
8 + 7 = 15
Correct! You took 3 seconds and earned 7 points.

...

========================================
TEST RESULTS
========================================
Final Score: 32
Correct Answers: 4/5 (80%)
Average Response Time: 4 seconds

Question Breakdown:
----------------------------------------
Question   Correct     Time
----------------------------------------
Q1         YES           3s
Q2         YES           2s
Q3         NO            8s
Q4         YES           5s
Q5         YES           2s
----------------------------------------
```



