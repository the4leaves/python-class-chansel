addorremove = 0
print('First youy will be asked if you want to add or remove an item. Then input the item you would like to add or remove. Type \"list\" if you want the code to list the items currently on your list. Type \"clear\" in the add/remove bar to clear your list. Finally type \"stop\" in the add/remove bar if you want to quit the program')
glist = []
while True:
        addorremove = input(print('print \"add\" or \"remove\" '))
        if addorremove == str('add'):
            glist.append(input(print('adding... ')))
        elif addorremove == str('remove'):
            glist.remove(input(print('removing... ')))
        elif addorremove == str('list'):
            print(glist)
        elif addorremove == str('clear'):
            glist = []
        elif addorremove == str('stop'):
            input(print('press any key to exit... '))
            break
        else:
            print('incorrect input')