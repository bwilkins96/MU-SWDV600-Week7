# Produces a .txt file of random shape specifications that works with 'shape_painter.py'

from random import random, randrange

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

def get_random_points():
    coords = (randrange(0, 500), randrange(0, 500))
    return f'{coords[0]}, {coords[1]}'

def get_random_color():
    r = randrange(192, 255) 
    g = randrange(192, 255)
    b = randrange(192, 255)

    return f'{r}, {g}, {b}'

def get_random_rect():
    name = 'Rectangle'
    ul_point = get_random_points()
    lr_point = get_random_points()
    color = get_random_color()

    return f'{name}; {ul_point}; {lr_point}; {color}'

def get_random_circle():
    name = 'Circle'
    center_point = get_random_points()
    radius = randrange(5, 100)
    color = get_random_color()

    return f'{name}; {center_point}; {radius}; {color}'

def main():
    file_name, num_shapes = get_input()
    shapes_file = open(file_name, 'w')

    for i in range(num_shapes):
        if random() < 0.5:
            shape_str = get_random_rect()
        else:
            shape_str = get_random_circle()
        
        print(shape_str, file=shapes_file)

    shapes_file.close()
    print(f'\nFinsihed writing to {file_name}')
    return file_name

if __name__ == '__main__': main()