from datetime import datetime
birth_year = input('Enter your birh year!')
age = datetime.now().year - int(birth_year)
print("Age: " + str(age))
