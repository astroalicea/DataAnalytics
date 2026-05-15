# Open and read the full file
f = open('about_me.txt', 'r')

#Next 4 lines using readline()
first_50 = f.read(50)

#Next 4 lines using readline()
next_four = []
for i in range(4):
    next_four.append(f.readline())

#Remaining lines using readlines()
last_chunk = f.readlines()

f.close()
print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {next_four}")
print(f"Next 100 characters, as list by line, rounded up to complete lines {last_chunk}")