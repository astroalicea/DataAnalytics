# Movie list

movie_list = [
    'Once Upon A Time In Hollywood', 'Kill Bill', 'Kill Bill Vol.2', 'There Will Be Blood',
    'The Truman Show', 'No Country For Old Men', 'Into The Wild', 'All Quiet On The Western Front', 'Chungking Express', 'The Lord of the Rings: The Return of the King'
]

print("The list movie_list includes my top", len(movie_list), "favorite movies.")
print(movie_list)

print(sorted(movie_list)) #returns a new srted list without changing the original

movie_list.sort() #.sort() modifies the original list and returns None.
print(movie_list)

movie_list.append('Gladiator')
print(f"The list movie list now includes my top {len(movie_list)} favorite moives.")
print(movie_list)