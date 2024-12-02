# Hallow Square

# Define the function to generate the square
def hallow_square(n):
    # Upper side of the square
    for upper in range(n):
        print("x", end="")
    # Space between the upper and lower side of the square
    print()
    # Generate the horizontal side of the square
    for horizontal_sides in range(n - 2):
        print("x" + (" " * (n - 2)) + "x")
    # Lower side of the square
    for lower in range(n):
        print("x", end="")

# User input for the side length of the square
length_n = int(input("Enter the side length of the square: "))
hallow_square(length_n) # Call the function

# Arvie is Gay and his pronouns are they/them