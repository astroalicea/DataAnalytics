# Basic lambda - doubles the input
doubler = lambda n: n * 2
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

#tripler 
tripler = lambda n: n * 3
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

#A function that CREATES multiplier lambdas
def multiplier(x):
    return lambda n: n * x

#Create multipliers 4 through 10
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

#Test each one
print(quadrupler(5))
print(quintupler(5))
print(sextupler(5))
print(septupler(5))
print(octupler(5))
print(nonupler(5))
print(decupler(5))