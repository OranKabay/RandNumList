import random
list = []
for i in range(100):
    list.append(random.randrange(1,101,1))
    list.sort()
    print(list)  