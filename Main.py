def check_value_in_dict(dictionary, value):
    return value in dictionary.values()

# Example dictionary
sample_dict = {
    'a': 100,
    'b': 200,
    'c': 300
}

# Check if 200 is in the dictionary
if check_value_in_dict(sample_dict, 200):
    print("200 is in the dictionary.")
else:
    print("200 is not in the dictionary.")