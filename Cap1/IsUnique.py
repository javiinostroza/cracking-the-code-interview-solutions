'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''

def is_unique_v1(word): # => O(n**2 * log(n))
    length = len(word)
    list_ = []

    for l in word: # O(n)
        if l in list_: # O(n*log(n)) + O(log(n))
            return False
        list_.append(l)
    return True

def is_unique_v2(word): # O(3n)
    let = {}
    for l in word:
        let[l] = 0

    for l in word:
        let[l] += 1

    for key in let.keys():
        if let[key] > 1:
            return False

    return True


# Tests made by @chamox
if __name__ == "__main__": 

    functions = [
                 is_unique_v1,
                 is_unique_v2
                ]
    
    test_cases = [
                  ("abcdef", True),
                  ("aabxxd", False),
                  ("DEF",True),
                  ("dDeE", False)
                 ]

    for function in functions:
        print("testing",function.__name__,":")

        for text,result in test_cases:
            print(function(text) == result)
 
        print("\n")