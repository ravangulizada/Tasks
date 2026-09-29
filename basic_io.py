name = input("Enter your name: ")
age = int(input("Enter your age: "))
fav_number = int(input("Enter your favorite number: "))
new_age = age + 10
new_fav_number = fav_number ** 2
if fav_number % 2 == 0:
    value_fav_number = 'even'
else:
    value_fav_number = 'odd'
print(f'Hi {name}! In 10 years you\'ll be {new_age}. Your favorite number squared is {new_fav_number}, and it\'s {value_fav_number}.')