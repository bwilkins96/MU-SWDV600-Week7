# Produces a .txt file of random shape specifications that works with 'shape_painter.py'

from random import random, randrange

# gets and validates user input for file and number of shapes to make
def get_input():
    file_name = input('Enter the drawing file name to create: ')

    if len(file_name) == 0: 
        file_name = 'random_shapes.txt'

    while True:
        try:
            num_shapes = int(input('Enter the number of shapes to make: '))
            break
        except:
            print('Invalid input')

    return file_name, num_shapes

# Returns a coordinates string using random coordinates 
def get_random_points(name):
    max_height = 500
    max_width = 500

    # Gets different coordinates based on shape name
    if name == 'Rectangle':
        coords = (randrange(1, max_height-1), randrange(1, max_width-1))
    else:
        offset = 70
        coords = (randrange(offset, max_height-offset), randrange(offset, max_width-offset))
    
    return f'{coords[0]}, {coords[1]}'

# Returns an rgb string with values between 192 and 255
def get_random_color():
    r = randrange(192, 255) 
    g = randrange(192, 255)
    b = randrange(192, 255)

    return f'{r}, {g}, {b}'

# Returns a string specifying a rectangle
def get_random_rect():
    name = 'Rectangle'
    ul_point = get_random_points(name)
    lr_point = get_random_points(name)
    color = get_random_color()

    return f'{name}; {ul_point}; {lr_point}; {color}'

# Returns a string specifying a circle
def get_random_circle():
    name = 'Circle'
    center_point = get_random_points(name)
    radius = randrange(5, 70)
    color = get_random_color()

    return f'{name}; {center_point}; {radius}; {color}'

# Main function that starts execution of program
def main():
    file_name, num_shapes = get_input()
    shapes_file = open(file_name, 'w')

    for i in range(num_shapes):
        # Randomly produces either a rectangle or circle string
        if random() < 0.5:
            shape_str = get_random_rect()
        else:
            shape_str = get_random_circle()
        
        # Writes shape string to file
        print(shape_str, file=shapes_file)

    shapes_file.close()
    print(f'\nFinsihed writing to {file_name}')

    # Returns file name for use in interface with 'shape_painter.py'
    return file_name

if __name__ == '__main__': main()