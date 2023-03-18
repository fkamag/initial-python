def higher_number(x, y):
    if x > y:
        return x
    else:
        return y


def average(list):
    count = 0
    for i in list:
        count += i
    return count / len(list)


def asterisk(n):
    for i in range(n):
        print(n*'*')
    return


def bigger(words):
    word_big = 0
    word_index = 0
    index = -1
    for word in words:
        index += 1
        if len(word) > word_big:
            word_big = len(word)
            word_index = index
    return words[word_index]


def paint_wall(n):
    if n % 54 == 0:
        latas = n / 54
        valor = latas * 80
        return (latas, valor)
    latas = n // 54 + 1
    valor = latas * 80
    return (latas, valor)
