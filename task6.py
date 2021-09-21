a=int(input('insert first side:'))
b=int(input('insert second side:'))
c=int(input('insert third side:'))
p=(a+b+c)/2
area=(p*(p-a)*(p-b)*(p-c))**0.5
print(area)