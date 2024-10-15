# Function to compare two strings
def compare_strings(str1, str2):
    if str1 == str2:
        return "The strings are identical."
    else:
        return "The strings are different."

# Example usage
string1 = "Hello, World!"
string2 = "Hello, World!"

result = compare_strings(string1, string2)
print(result)
