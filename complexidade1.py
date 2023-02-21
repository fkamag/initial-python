from time import time

def calculations(n):
    inicial1 = time()
    number1 = 0
    for n1 in range(n):
        number1 += n1
    final1 = time()
    print ((final1 - inicial1)*1000)

    inicial2 = time()
    number2 = 0
    for n1 in range(n):
        for n2 in range(n):
            number2 += n1 + n2
    final2 = time()
    print ((final2 - inicial2)*1000)

    inicial3 = time()
    number3 = 0
    for n1 in range(n):
        for n2 in range(n):
            for n3 in range(n):
                number3 += n1 + n2 + n3
    final3 = time()
    print ((final3 - inicial3)*1000)

    return number1, number2, number3

n1, n2, n3 = calculations(100)
print(f'{n1}, {n2}, {n3}')