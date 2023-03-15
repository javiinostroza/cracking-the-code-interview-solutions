'''
Given a string, write a function to check if it is a permutation of a palin­drome. 
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.
'''

# If a palindrome has pair length, all the characters must to be in pair quantities.
# If a palindrome has odd length, there is only one character with odd quantity 
# and the others must to be in a pair quantities.

# Also we have that in a pair length palindrome, we have the same characters in same quantity in both halves 
# of the string. In addition, for an odd length palindrome, we need to have in the middle of the string the character in 
# odd quantity and since this character the left and right middle have the same chars in same quantities.

def PalindromePermutation(string_: str) -> bool:

    chars_quantity = {}
    # Save the quantity for every char in the string
    for char in string_.replace(" ", "").lower():
        if char in chars_quantity.keys():
            chars_quantity[char] += 1
        else:
            chars_quantity[char] = 1
    odd_chars = 0
    # Check if at most 1 char is in odd quantity
    for char, quantity in chars_quantity.items():
        if quantity%2:
            odd_chars += 1
        if odd_chars > 1:
            return False
    return True


# Tests made by @chamox    
if __name__ == "__main__":

    test_cases = [
                    ("aba", True),
                    ("aab", True),
                    ("abba", True),
                    ("aabb", True),
                    ("a-bba", True),
                    ("a-bba!", False),
                    ("Tact Coa", True),
                    ("jhsabckuj ahjsbckj", True),
                    ("Able was I ere I saw Elba", True),
                    ("So patient a nurse to nurse a patient so", False),
                    ("Random Words", False),
                    ("Not a Palindrome", False),
                    ("no x in nixon", True),
                    ("azAZ", True),
                ]

    functions = [
                PalindromePermutation     
                ]


    for function in functions:
    
        print("testing",function.__name__,":")

        for text,expected in test_cases:

            print(function(text) == expected)
            assert function(text) == expected

        print("\n") 