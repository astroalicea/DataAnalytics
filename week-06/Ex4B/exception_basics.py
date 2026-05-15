# ValueError - happens when wrong value type is given

try:
    x = int('hello')
except ValueError:
    print("ValueError: Cannot convert 'hello' to an integer")
else:
    print(x)
finally:
    print("Let's try another one...  \n")

#NameError - happens when variable doesnt exist

try:
    m = banana
except NameError:
    print("NameError: Oops, looks like you tried to use an undefined variable")
else:
    print(m)
finally:
    print("Let's try another one... \n")

#TypeError - happnes when wrong data type is used

try:
    result = 'age: ' + 25
except TypeError:
    print("TypeError: Cannot add a string and an integer directly")
else:
    print(result)
finally:
    print("Lets try another one... \n")

#SyntaxError - happens when code is written incorrectly

try:
    eval('if True')
except SyntaxError:
    print("SyntaxError: Code is not written correctly")
else:
    print("No syntax error")
finally:
    print("Lets try another one... \n")