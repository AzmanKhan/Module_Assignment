
def reverse_string(s):
    """Return the reverse of the input string."""
    return s[::-1]

def capitalize_string(s):
    """Return the input string with the first character capitalized and the rest lowercased."""
    return s.capitalize()

def to_uppercase(s):
    """Return the input string in uppercase."""
    return s.upper()

def to_lowercase(s):
    """Return the input string in lowercase."""
    return s.lower()

def is_palindrome(s):
    """Check if the input string is a palindrome."""
    return s == s[::-1]
    