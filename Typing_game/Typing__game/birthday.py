from datetime import date

birth = input("Enter your birthday (MM-DD)")
month, day = map(int, birth.split("-"))

today = date.today()
next_birthday = date(today.year, month, day)

if next_birthday < today:
    next_birthday = date(today.year + 1, month, day)

days_left = (next_birthday - today).days
print(f"{days_left} days left to your next Birthday")