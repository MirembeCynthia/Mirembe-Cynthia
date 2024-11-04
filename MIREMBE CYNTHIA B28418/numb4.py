def syracuse_sequence(start):
    sequence = []
    while start != 1:
        sequence.append(start)
        if start % 2 == 0:
            start //= 2  # If even
        else:
            start = 3 * start + 1  # If odd
    sequence.append(1)  # Add the final 1
    return sequence

# Get user input
try:
    starting_value = int(input("Enter a natural number to generate the Syracuse sequence: "))
    if starting_value <= 0:
        print("Please enter a positive natural number.")
    else:
        result = syracuse_sequence(starting_value)
        print("The Syracuse sequence is:", result)
except ValueError:
    print("Please enter a valid integer.")
