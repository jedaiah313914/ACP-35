def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)

def print1to10():
    for i in range(1, 11):
        print(i)

n = 5
print(fac(n))
print1to10()