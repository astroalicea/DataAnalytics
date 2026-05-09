# Using enumerate. creating a ranked list.

countries_to_visit = [
    'Japan', 'Argentina', 'Brazil',  'New Zealand', 'Norway', 'Vietnam', 'South Korea', 'Thailand', 'France', 'Peru', 'Tanzania', 'Zimbabwe'
]

for index, item in enumerate(countries_to_visit, start=1):
    if index == 1:
        print(f"{index}. {item} <- top pick!")
    else:   
        print(f"{index}. {item}")