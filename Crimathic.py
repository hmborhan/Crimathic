import random
import time

def generate_problem(difficulty):
    """Generates a math problem based on difficulty level."""
    if difficulty == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-"])
        problem = f"{num1} {operator} {num2}"
        answer = eval(problem)
    elif difficulty == 2:
        num1 = random.randint(10, 50)
        num2 = random.randint(10, 50)
        operator = random.choice(["+", "-", "*"])
        problem = f"{num1} {operator} {num2}"
        answer = eval(problem)
    else:
        num1 = random.randint(50, 100)
        num2 = random.randint(50, 100)
        operator = random.choice(["+", "-", "*", "/"])
        problem = f"{num1} {operator} {num2}"
        answer = eval(problem)
    return problem, answer

def play_level(difficulty, time_limit):
    """Plays a single level of the game."""
    problem, answer = generate_problem(difficulty)
    print(f"Solve this problem: {problem}")
    start_time = time.time()

    # Countdown timer
    while time_limit > 0:
        print(f"Time left: {time_limit} seconds", end="\r")
        time.sleep(1)
        time_limit -= 1

        # Check if the player has answered
        if time.time() - start_time >= time_limit:
            print("\nTime's up!")
            return False

    print("\nTime's up!")
    return False

def main():
    difficulty = 1
    time_limit = 10  # Time limit in seconds
    level = 1

    while True:
        print(f"\n--- Level {level} ---")
        print(f"Difficulty: {difficulty}, Time Limit: {time_limit} seconds")
        if not play_level(difficulty, time_limit):
            print("Game Over! You ran out of time.")
            break
        level += 1
        difficulty += 1
        time_limit -= 1  # Decrease time limit as levels increase

if name == "main":
    main()


