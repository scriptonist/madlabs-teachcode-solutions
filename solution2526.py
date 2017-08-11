s = input()
fi = int(input())
si = int(input())

print(s[fi].upper())
print(s[si].lower())
l = list(map(ord,s))
print(sum(l))

