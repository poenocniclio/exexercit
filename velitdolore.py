# Prompt the user to enter a position within the range of 0-8
position = input("Please enter the position you want (0-8): ")

# Try to convert the input to an integer and validate it
try:
    position = int(position)
    if 0 <= position <= 8:
        print(f"You entered a valid position: {position}")
    else:
        print("Error: The position must be between 0 and 8.")
except ValueError:
    print("Error: Please enter a valid integer.")
