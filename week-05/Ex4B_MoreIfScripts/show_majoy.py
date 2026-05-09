# Displying major name and department office based on major code.

major_code = input("Enter major code: ")

if major_code == 'BIOL':
    print("Major: Biology, Office: Science Bldg, Room 310")
elif major_code == 'CSCI':
    print("Major: Computer Science, Office: Sheppard Hall, Room 314")
elif major_code == 'ENG':
    print("Major: English, Office: Kerr Hall, Room 201")
elif major_code == 'HIST':
    print("Major: History, Office: Kerr Hall, Room 114")
elif major_code == 'MKT':
    print("Major: Marketing, Office: Westly Hall, Room 310")
else:
    print("<unknown>")