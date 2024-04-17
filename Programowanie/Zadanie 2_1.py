def policz_liczbe_blokow(n):

    b = 0
    poprzednik = -1
    while n > 0:

        reszta = n % 2
        if poprzednik != reszta:
            b += 1

        poprzednik = reszta
        n //= 2
    return b

print(policz_liczbe_blokow(67))
print(policz_liczbe_blokow(64))