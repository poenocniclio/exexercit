import sys

# Check if there are more than three command-line arguments
if len(sys.argv) > 3:
    # If there are, assign the fourth argument to the variable auth_type
    auth_type = sys.argv[3]
else:
    # If there are fewer than four arguments, assign "WPA" to auth_type
    auth_type = "WPA"
