getinput = False
while getinput is False:
    try:
        speed = float(input('what is the minions speed? '))
        getinput = True
    except ValueError:
        print('wrong input')
getinput = False
while getinput is False:
    try:
        how_many = float(input('how many resources per action does it produce? '))
        getinput = True
    except ValueError:
        print('wrong input')
getinput = False
while getinput is False:
    try:
        numberofminions = float(input('how many minions are working? '))
        getinput = True
    except ValueError:
        print('wrong input')
getinput = False
while getinput is False:
    try:
        time = float(input('how many hours will you run them? '))
        getinput = True
    except ValueError:
        print('wrong input')
getinput = False
while getinput is False:
    enchanted = input('are you planning on turning the resources into there enchanted form? (Y or N) ')
    if (enchanted == 'Y'):
        getinput = False
        while getinput is False:
            try:
                evalue = float(input('how much is 1 enchanted item worth? '))
                getinput = True
            except ValueError:
                print('wrong input')
        actionsperminute = 60 / float(speed)
        itemsperminute = float(actionsperminute) * float(how_many)
        itemsperhour = float(itemsperminute) * 60
        itemstotal = (float(itemsperhour) * float(time)) / 160
        allminionitems = float(itemstotal) * float(numberofminions) / 2
        totalprofit = float(allminionitems) * float(evalue)
        print(str(allminionitems) + 'items')
        print(str(totalprofit) + ' in ' + str(time) + ' hours!')
        input('press any key to exit... ')
        getinput = True
    elif (enchanted == 'N'):
        getinput = False
        while getinput is False:
            try:
                value = float(input('how much is 1 item worth? '))
                getinput = True
            except ValueError:
                print('wrong input')
        actionsperminute = 60 / float(speed)
        itemsperminute = float(actionsperminute) * float(how_many)
        itemsperhour = float(itemsperminute) * 60
        itemstotal = (float(itemsperhour) * float(time))
        allminionitems = float(itemstotal) * float(numberofminions) / 2
        totalprofit = float(allminionitems) * float(value)
        print(str(totalprofit) + ' in ' + str(time) + ' hours!')
        input('press any key to exit... ')
        getinput = True
