#1. 
#Присвоємо значення двом змінним:

x = 10
y = -5

#2.
#Складемо чотири складних логічних вирази з оператором and:

exp1 = (x > 0) and (y > 0)  # Істинність обох
exp2 = (x > 0) and (y < 0)  # Перший істинний, другий хибний
exp3 = (x < 0) and (y > 0)  # Перший хибний, другий істинний
exp4 = (x < 0) and (y < 0)  # Хибність обох

#3. 
#Аналогічно виконаємо для оператора or:

exp5 = (x > 0) or (y > 0)  # Хоча б один істинний
exp6 = (x > 0) or (y < 0)  # Перший істинний
exp7 = (x < 0) or (y > 0)  # Другий істинний
exp8 = (x < 0) or (y < 0)  # Обидва хибні

#5. 
#Напишемо код, що виводить повідомлення в залежності від значення змінної:

if x > 0:
    print("Значення змінної x більше 0")
else:
    print("Значення змінної x менше або дорівнює 0")

#6.
#Додамо гілку else:
if x > 0:
    print("1")
elif x < 0:
    print("-1")
else:
    print("0")