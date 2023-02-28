# Produces a window with random shapes
# Interfaces between 'random_shapes.py' and 'shape_painter.py'

import shape_painter as sp
import random_shapes as rs

def main():
    fileName = rs.main()
    print('-'*15)

    drawingFile = open(fileName, 'r')
    shapes = sp.getShapes(drawingFile)
    drawingFile.close()

    sp.drawShapes(shapes)

if __name__ == '__main__': main()