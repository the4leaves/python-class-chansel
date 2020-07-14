gradestotal = 0
y = 0
z = 0
grade = 0
while True:
    tempgrade = input('input grade percentage... ')
    try:
        tempgrade = int(tempgrade)
    except:
        if tempgrade == 'stop':
            break
        else:
            print('type in stop or a grade percent without the sign... ')
    gradestotal += 1
    grade += tempgrade
y = grade / gradestotal
y = round(y)
print ('Your average grade is ' + str(y) + ' percent')

if y >= 97:
    print ('thats an A+!')
elif y >= 94:
    print ('thats an A!')
elif y >= 90:
    print ('thats an A-!')
elif y >= 87:
    print ('thats an B+!')
elif y >= 84:
    print ('thats an B!')
elif y >= 80:
    print ('thats an B-!')
elif y >= 77:
    print ('thats an C+!')
elif y >= 74:
    print ('thats an C!')
elif y >= 70:
    print ('thats an C-!')
elif y >= 67:
    print ('thats an D+!')
elif y >= 64:
    print ('thats an D!')
elif y >= 60:
    print ('thats an D-!')
else:
    print ('thats an F!')
       
input('press any key to quit... ')