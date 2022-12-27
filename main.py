from pprint import pprint
import array
from math import cos, sin, pi, radians

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

class Triangle:
    def __init__(self, points):
        self.points = points
        
class Hexagon:
    def __init__(self, x, y, l, r, g, b):
        self.center = Point2D(x, y)
        self.l = l
        self.r = r
        self.g = g
        self.b = b
        self.vertexes = self.generate_vertexes()
        # self.triangles = self.generate_triangles()
    
    def generate_vertexes(self):
        vertexes = []
        
        for angle in range(0, 360, 60):
            vertexes.append(self.center + Point2D(self.l * cos(radians(angle)), self.l * sin(radians(angle))))
        
        return vertexes
        
    def print_data(self):
        print(self.center)
        
    def print_vertexes(self):
        for vertex in self.vertexes:
            print(vertex)

def read_input_file(filename):
    hexagons = []
    
    with open(filename, 'r') as file:
        n = int(file.readline())
        for _ in range(n):
            parameters = file.readline().split(" ")
            for i in range(len(parameters) - 1):
                parameters[i] = int(parameters[i])
            parameters[-1] = int(parameters[-1].replace('\n', '')) 
            x, y, l, r, g, b = parameters
            hexagons.append(Hexagon(x, y, l, r, g, b))
        
    return hexagons

hexagons = read_input_file("in.txt")
hexagons[0].print_vertexes()

# HEIGHT = 1024
# WIDTH = 960

# red = [0] * (HEIGHT * WIDTH)
# green = [0] * (HEIGHT * WIDTH)
# blue = [0] * (HEIGHT * WIDTH)

# for i in range(HEIGHT):
#     for j in range(WIDTH):
#         for circle in circles:
#             if(circle.point_in_circle(i, j)):
#                 red[i * WIDTH + j] = circle.rgb[0]
#                 green[i * WIDTH + j] = circle.rgb[1]
#                 blue[i * WIDTH + j] = circle.rgb[2]


# def writePPM(red, green, blue, width, height, filename):
#     # todo archivo necesita una cabecera, en PPM la cabecera inicia con P6 e indica el anchoe, alto y valor maximo
#     ppm_header = f'P6 {width} {height} {255}\n'
#     rgb = []
#     for i in range(len(red)):
#         rgb.append(red[i]) # Red 
#         rgb.append(green[i]) # Green 
#         rgb.append(blue[i]) # Blue
#     image = array.array('B', rgb)

#     with open(filename + '.ppm', 'wb') as f:
#         f.write(bytearray(ppm_header, 'ascii'))
#         image.tofile(f)
    
# writePPM(red, green, blue, WIDTH, HEIGHT, "mi_circulo")