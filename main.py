# lists
suspects = ['Jay', 'Megan', 'Abriella']
rooms = ['living room', 'bedroom 1', 'bedroom 2']
found_items = ['notebook']
missing_items = ['golden key', 'silver key', 'cup']

rooms = {
'Dining room': 'where the murder happened',
'Back door': {'well': 'poison bottle'},
'Lilian\'s bedroom': {'bedside table': 'little key'},
'Lilian\'s office': {'fireplace': 'note', 'safe': 'bronze key'},
'Jay\'s bedroom': {'coat hanger': 'recipt'},
'Megan\'s bedroom': {'under the bed': 'notebook'},
'Abriella\'s bedroom': 'nothing'
}

characters = {
'Lilian': {'age': 'in her 60s', 'illness': 'heart problems'},
'Jay': {'age': 'in his 30s', 'illness': 'high blood pressure'},
'Megan': {'age': 'in her 30s', 'illness': 'no illness'},
'Abriella': {'age': 'in her 20s', 'illness': 'asthma'}
}
for person, description in characters.items():
    print(f"{person}:")
    age = f"{description['age']}"
    illness = f"{description['illness']}"
    print(f"\t{person} is {age}.")
    print(f"\t{person} has {illness}.")
