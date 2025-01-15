def extract_numbers(input_string):
    numbers = ''.join(filter(str.isdigit, input_string))
    return numbers

# Ask the user for input
input_string = input("Enter a word with numbers: ")

# Extract and print the numbers
print(extract_numbers(input_string))