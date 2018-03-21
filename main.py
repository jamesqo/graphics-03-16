from display import *
from draw import *
from theparser import parse_file
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )
