import random

getinput = False
while getinput is False:
    try:
        x = float(input('input a number... '))
        getinput = True
    except ValueError:
        print('I said a NUMBER!')
y = (random.randrange(1, 100))
print (x + y)