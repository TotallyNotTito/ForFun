import math
import random

count = 0
area = 0
height = float(input("starting height\n"))
base = float(input("starting base\n"))
numtriangles = int(input("How many triangles\n"))
while (count < numtriangles):
  area = area + (base * height)/2
  base = math.sqrt(height**2 + base**2)
  count = count + 1
  #print(area)
print(area)
