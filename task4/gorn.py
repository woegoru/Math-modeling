res = 0
n = float(input())
x = float(input())
while n > 0:
    coef = float(input())
    res += coef
    res *= x
    n -= 1
coef = float(input())
res += coef
print(res)