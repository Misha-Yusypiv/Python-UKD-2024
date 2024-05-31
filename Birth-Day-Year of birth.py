#8

year = int(input("Введіть рік: "))

if 2016 <= year <= 2024:
    zodiac_signs = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"]
    sign_index = (year - 2016) % 12
    print("Знак зодіаку для року {}: {}".format(year, zodiac_signs[sign_index]))
else:
    print("Рік не входить у діапазон 2016-2024")
