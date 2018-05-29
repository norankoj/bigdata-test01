from random import randint

nlist =[]
for no in range(0,5):
    randomNum = randint(1, 45)
    nlist.append(randomNum)

nlist.append(randint(1, 45))
s = set(nlist)