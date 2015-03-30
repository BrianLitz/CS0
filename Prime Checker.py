def primeCheck(number):
    for x in range(2,number):
        if number %x==0:
            return False
    return True






pList=[]
for n in range(3,1000):
    if primeCheck(n):
        pList.append(n)

print pList, sum(pList)