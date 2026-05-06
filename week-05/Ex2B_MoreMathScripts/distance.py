#  Calcualte distance between coordinates
import math

x1 = 234.5
x2 = 984.3

y1 = 1000.9
y2 = 1400.6

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"The distance between the two points is {distance:.2f}")