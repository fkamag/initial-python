from random import randrange

def random_mean(number):
    array = []
    itens = 100
    for _ in range(itens):
        sum = 0
        for _ in range(number):
            sum += randrange(1, number)
        med = sum / number
        array.append(med)

    return array

result = random_mean(10)
print(result)
