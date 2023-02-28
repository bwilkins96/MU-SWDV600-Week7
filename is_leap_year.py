# Function that returns whether a year is a leap year
# A leap year is divisible by 4, unless it is a century year that is not divisible by 400
# Developed in a spiral/prototyping fashion

def test():
    # Tests 1
    print(is_leap_year(2016))    # -> True
    print(is_leap_year(2015))    # -> False

    # Tests 2
    print()
    print(is_leap_year(1800))    # -> False
    print(is_leap_year(1900))    # -> False
 
    # Tests 3
    print()
    print(is_leap_year(1600))    # -> True
    print(is_leap_year(2000))    # -> True


# Iteration 3
def is_leap_year(year):
    if year % 4 == 0:
        if (year % 100 == 0) and (year % 400 != 0):
            return False
        else:
            return True
    else:
        return False

if __name__ == '__main__': test()

# Iteration 1
#------------------------
# def is_leap_year(year):
#     if year % 4 == 0:
#         return True
#     else:
#         return False

# Iteration 2
#------------------------
# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             return False

#         return True
#     else:
#         return False