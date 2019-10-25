enter_name = input('What is your name? ')
name = len(enter_name)

if name < 3:
    print('Name must be at least 3 characters')
elif name > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good!')