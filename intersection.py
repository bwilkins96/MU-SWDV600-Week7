# Function that returns a string of common characters between 2 strings
# Bottom-up design using test cases

def test():
    print(intersection('hello', 'world'))     # -> 'lo'
    print(intersection('unique', 'rock'))     # -> ''
    print(intersection('canada', 'canine'))   # -> 'can'

def intersection(str1, str2):
    common_chars = ''

    for char in str1:
        if (char in str2) and (char not in common_chars):
            common_chars += char

    return common_chars

if __name__ == '__main__': test()