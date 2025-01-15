def replace_the_symbols(text):
    result = ''
    for char in text:
        if not char.isalnum():  # Checks if the character is not a letter or number
            result += ' #'
        else:
            result += char
    return result

input_text = input("Say something... and add any symbol you add it will be turned into magic: ")
output_text = replace_the_symbols(input_text)
print(output_text)
