def zadanie1(a_list, b_list):
    new_list = []
    if len(a_list) < len(b_list):
        length = len(a_list)
        big=b_list
    else:
        length = len(b_list)
        big=a_list
    for x in range (len(big)):
        if(x>=length):
            new_list.append(big[x])
        else:

            if x % 2 == 0:
                new_list.append(a_list[x])
            else:
                new_list.append(b_list[x])
    return new_list

a=[1,2,3,8,6,9]
b=[4,3,2,7,9,5]

print(zadanie1(a,b))