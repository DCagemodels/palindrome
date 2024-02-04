import sys

def is_palindrome(userInputString):
    # Preprocess the string: Convert to lowercase and filter out non-alphanumeric characters
    processed_string = " ".join(char.lower() for char in userInputString if char.isalnum())

    # Check if the processed string is equal to its reverse
    if processed_string == processed_string[::-1]:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome!")

if __name__ == "__main__":
    # Check if the user provided an argument (excluding the script name)
    if len(sys.argv) != 2:
        print("Usage: python palindrome.py <userInputString>")
    else:
        userInputString = sys.argv[1]
        is_palindrome(userInputString)