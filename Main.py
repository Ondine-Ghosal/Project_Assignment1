def isAnagram(s: str, t: str) -> bool:
    s_cleaned = ''.join(s.lower().split())
    t_cleaned = ''.join(t.lower().split())
    return sorted(s_cleaned) == sorted(t_cleaned)

# User input for two strings
s = input("Enter the first string: ")
t = input("Enter the second string: ")

# Check and display if they are anagrams
if isAnagram(s, t):
    print("The strings are anagrams.", True)
else:
    print("The strings are not anagrams.", False)
