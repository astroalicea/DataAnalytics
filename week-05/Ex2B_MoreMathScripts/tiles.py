# calculating amount of tiles needed for a room
import math 

length = 29

width = 21

area = length * width

tiles_needed = math.ceil(area * 1.10)

boxes_needed = math.ceil(tiles_needed / 12)

print(f"The room is {length} x {width} feet")
print(f"You need {tiles_needed} tiles. *10% is included")
print(f"You will need to buy {boxes_needed} boxes of tiles")

