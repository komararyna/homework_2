n=int(input('insert your number:'))
digc=0
while n>0:
    digc += 1
    n=n//10
print(digc)