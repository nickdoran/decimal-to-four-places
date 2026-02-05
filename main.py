import subprocess

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
    rounded_number = round(float(user_input), 4)
    str_rounded_number = str(rounded_number)
    print(str_rounded_number)
    try:
        subprocess.run("pbcopy", text=True, input=str_rounded_number, check=True)
        print("Copied to Clipboard")
    except subprocess.CalledProcessError:
        print("Failed to copy to clipboard")

print("quitting application")
