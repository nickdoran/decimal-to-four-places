def is_valid_input(value):
    """Check if input is 'quit' or a valid number (int or float)."""
    if value.lower() == "quit":
        return True
    try:
        float(value)
        return True
    except ValueError:
        return False

while True:
    user_input = input("Enter a number or 'quit': ")

    if user_input.lower() == "quit":
        break

    if not is_valid_input(user_input):
        print("Invalid input. Please enter a number or 'quit'.")
        continue

    print(round(float(user_input), 4))

print("quitting application")
