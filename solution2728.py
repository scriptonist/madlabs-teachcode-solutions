n = int(input())
l = []

for i in range(n):
    inp = input().split(" ")
    op = inp[0]
    args = []
    if len(inp) > 1:args = list(map(int,inp[1:]))

    if op == "append":
        l.append(args[0])
    elif op == "insert":
        l.insert(args[0],args[1])
    elif op == "print":
        print(l)
    elif op == "pop":
        l.pop()
    elif op == "remove":
        l.remove(args[0])
    elif op == "reverse":
        l.reverse()
    elif op == "sort":
        l.sort()
    