x =[1,3,3,2,4,5]
def ListSimplifier(x):
    repeat_values = []
    final_list = []
    for element in x:
        if element not in repeat_values:
            final_list.append(element)
            repeat_values.append(element)
    return final_list
ListSimplifier(x)
print (ListSimplifier(x))