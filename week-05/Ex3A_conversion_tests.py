# Description: This script tests various numeric
#       conversion technigues.
# Author: Luis Alicea

# 2
a = "   101.1"
b = '55'
c = "402 Stevens"
d = 'Number 5   '
# 3
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# print(int(a)) ValueError: invalid internal
print(int(b))
# print(int(c)) ValueError: invalid internal
# print(int(d)) ValueError: invalid internal

print(float(a))
print(float(b))
# print(float(c)) ValueError: could not convert string to float
# print(float(d)) ValueError: could not convert string to float

# 5
print(int(float(a)))

print(int(c[0:3]))

print(int(d[7:8]))

print(a.strip())
print(d.strip())
