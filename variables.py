from datetime import datetime


year_of_birth = int(input("Enter year of birth:"))
current_year = date.today().year
current_age = current_year - year_of_birth


if current_age < 18:
      print("you are a minor,")
elif 18<=current_age<36:
    print("you are a youth,")
else:
    print("you are elders,")