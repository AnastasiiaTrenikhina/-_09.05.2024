def test(name,year, txt = ' родилась'):
    print(name, "в", year ,'году' + txt)

test('Настя',1990 )


def fac(n):
    if n == 1:
        return 1
    return fac (n-1)*n
print(fac(3))
print(fac(5))

