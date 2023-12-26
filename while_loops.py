print('Restaurant Menu: ')
print('\tchoose your option:')
print('\t01- milk')
print('\t02- coffee')

choice = input('What do you want to eat ? ')

count = 0;

while(count < 5): 
    if choice == 'milk': 
        print('That would be 70t.')
    elif choice == 'coffee':
        print('That would be 45t.')
    else:
        print('We do not have this option')
    count += 1