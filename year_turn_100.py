def main():
    # Get the user's name and age
    name = input("What's your name? ")
    age = int(input("How old are you? "))

    # Calculate the year when the user will turn 100
    current_year = 2023  # You can also use Python's datetime module to get the current year dynamically
    year_turn_100 = current_year + (100 - age)

    # Print the result
    print(f"Hello, {name}! You will turn 100 years old in {year_turn_100}.")

if __name__ == "__main__":
    main()
