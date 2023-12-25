# working with input and output

name = input('Name: ')
age_string = input('Age : ');

age = int(age_string)

birth_year = 2023 - age

# string formating 
print(f'{name} is a {age_string} years old which means born in {birth_year}.')
print('{} is a {} years old which means born in {}.'.format(name, age_string, birth_year))