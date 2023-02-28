# Function that returns the difference in length between 2 strings
# Bottom-up design using test cases

def test():
    print(string_difference('abcd', 'abcd'))     # -> 0
    print(string_difference('hey', 'world!'))    # -> 3

def string_difference(str1, str2):
    return abs(len(str1) - len(str2))

if __name__ == '__main__': test()