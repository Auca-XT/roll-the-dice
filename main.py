import random

dice1 = ['1', '2', '3',
         '4', '5', '6']

rolldice = ""

for x in range(1):
  rolldice = rolldice + random.choices(dice1)[0]

print('Dice roll out come:\n', rolldice)