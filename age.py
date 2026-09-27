from datetime import datetime as dt

def calculate_age():
    birthdate = dt.strptime(input('Please enter a birthdate (DD-MM-YYYY): '), '%d-%m-%Y').date()

    current_date = dt.today().date()

    age = current_date.year - birthdate.year

    #Take into account if their birthday has not already passed this year
    if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):
        age -=1

    return(age)

age = calculate_age()
print(age)

