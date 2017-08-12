def change(a,b):

    a = b
    print(a)

l1 = []
l2 = []
for _ in range(int(input())):
    l1.append(int(input()))

for _ in range(int(input())):
    l2.append(int(input()))


change(l1,l2)
print(l1)
