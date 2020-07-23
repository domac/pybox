import copy

t1 = (1,2, [30,40])
t2 = (1,2, [30,40])
t3 = copy.copy(t1)
t4 = copy.deepcopy(t1)

print(id(t1))
print(id(t2))
print(id(t3))
print(id(t4))
print("------------")

print(t1==t2)
print(t1 is t2)

print(t1==t3)
print(t1 is t3)


print(t1==t4)
print(t1 is t4)

t1[-1].append(50)

print(t1)
print(t2)
print(t3)
print(t4)