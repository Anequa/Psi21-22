lista=[1,2,3,4,5,6,7,8,9,10]
temp=lista[5:]
lista=lista[:5]
print(temp)
print(lista)
suma=lista+temp
suma.insert(0,0)
print(suma)