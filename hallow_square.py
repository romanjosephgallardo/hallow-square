'''
Generate a hollow square based on the + integer input side length n.

Enter the side length of the square: 6
xxxxxx
x    x
x    x
x    x
x    x
xxxxxx

'''

# pseudocode
# User input for the side length of the square
length_n = int(input("Enter the side length of the square: "))

# Loop to generate the square
# Upper side of the square
for i in range(length_n - 1):
    print("x", end="")

# Generate the horizontal side of the square
for i in range(length_n -1):
    print("x" + " " * (length_n - 2) + "x")

# Lower side of the square
for i in range(length_n - 1):
    print("x", end="")

# Generate the hollow square