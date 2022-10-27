
def fatorial(n):
    """
        Calculates a fatorial of n using while loop
    """
    
    if n == 0:
        return 1
    else:
        fatorial = 1
        while n > 1:
            fatorial *= n
            n -= 1
        return fatorial
    
def fatorial_rec(n):
    """
        Calculates a fatorial of n using recursion
    """
    
    if n == 0:
        return 1
    else:
        return n * fatorial_rec(n-1)

print(fatorial(10))
print(fatorial_rec(10))