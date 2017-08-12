d = {}
for _ in range(int(input())):
    inp = input().split(" ")
    key = inp[0]
    vals = list(map(float,inp[1:]))
    d[key] = vals
name = input()
print("%.2f"%float(sum(d[name])/3))
