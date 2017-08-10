def isPrime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for n in range(2,int(number/2)+1):
        if number%n == 0:
            return False
    return True

r1 = int(input())
r2 = int(input())

for n in range(r1,r2+1):
    if isPrime(n) == True:
        print(n)
