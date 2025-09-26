import random

''' give output as number b/w the reange'''

# num = random.randint(1, 20)
# print(num)

low = 1
high = 10
options = ('rock', 'paper', 'scissor')
cards = ['1','2','3', '4','5','6','7','8','9','10','K','Q','J','A']
# num = random.randint(low, high)

# num = random.random()
'''give output as point values like 0.4005620431514263'''
# print(num)


# option = random.choice(options)
# print(option)

random.shuffle(cards)
print(cards)
