import random

dice1 = ['1', '2', '3',
         '4', '5', '6']

rolldice = ""

for x in range(1):
  rolldice = rolldice + random.choices(dice1)[0]

print('Dice roll out come:\n', rolldice)

print('\n', "other dice", '\n')

#dice with range a, b

for a in range(1,10):
 Worp = random.randint(1,6)
print("Worp",a, "was:", Worp)
