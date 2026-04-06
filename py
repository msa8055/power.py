def myPow(x, n):
    if n == 0:
        return 1.0
    
    if n < 0:
        x = 1 / x
        n = -n
    
    result = 1.0
    
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    
    return result


x, n = input().split()
x = float(x)
n = int(n)

ans = myPow(x, n)
print(f"{ans:.5f}")
