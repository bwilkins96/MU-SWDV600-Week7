# Draws shapes to a window based on lines in an inputted file

from graphics import Point, Circle, Rectangle, GraphWin, color_rgb

def getColor(colorStr):
    tokens = colorStr.split(',')

    if len(tokens) == 3:
        return color_rgb(int(tokens[0]), int(tokens[1]), int(tokens[2]))
    elif len(colorStr) > 0:
        return colorStr.strip()
    else:
        return 'white'

def getPoint(pointStr):
    x, y = pointStr.split(',')
    return Point(int(x), int(y))

def getRadius(radiusStr):
    return int(radiusStr)

def parseRectangleLine(line):
   shapeStr, ulStr, lrStr, colorStr  = line.split(';')
   
   ulPoint = getPoint(ulStr)
   lrPoint = getPoint(lrStr)
   color = getColor(colorStr)

   rectangle = Rectangle(ulPoint, lrPoint)
   rectangle.setFill(color)

   return rectangle

def parseCircleLine(line):
    shapeStr, cpStr, radiusStr, colorStr  = line.split(';')

    centerPoint = getPoint(cpStr)
    radius = getRadius(radiusStr)
    color = getColor(colorStr)

    circle = Circle(centerPoint, radius)
    circle.setFill(color)

    return circle

def getShapeName(line):
    tokens = line.split(';')
    return tokens[0]

def getShapes(drawingFile):
    shapes = []
    lineNum = 0

    for line in drawingFile:
        lineNum += 1
        shapeName = getShapeName(line)

        shape = None
        if shapeName.casefold() == 'circle'.casefold():
            shape = parseCircleLine(line)
        elif shapeName.casefold() == 'rectangle'.casefold():
            shape = parseRectangleLine(line)
        else:
            raise ValueError('ERROR on line {0}: Invalid shape {1}'.format(lineNum, shapeName))

        shapes.append(shape) 

    return shapes

def drawShapes(shapes):
    win = GraphWin('Drawing', 500, 500)

    for shape in shapes:
        shape.draw(win)

    print('Press "q" to close window')

    while True:
        press = win.getKey()
        if press == 'q': break

    win.close()

def main():
    fileName = input('Enter the drawing file name: ')
    drawingFile = open(fileName, 'r')

    shapes = getShapes(drawingFile)
    drawingFile.close()

    drawShapes(shapes)

if __name__ == '__main__': main()