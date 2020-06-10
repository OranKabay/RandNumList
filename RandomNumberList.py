import random
x = []
for i in range(100):
    x.append(random.randrange(1,101,1))
print(x)
x.sort()
print("\n")
print(x)
x = list(dict.fromkeys(x))
print("\n")
print(x)