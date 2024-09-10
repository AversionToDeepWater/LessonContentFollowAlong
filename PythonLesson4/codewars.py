import random

list = []

for i in range(0,5):
    n = random.randint(1,50)
    list.append(n)

if len(list) == 0:
    print(0)
else:
    print(sum(list))