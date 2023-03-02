# 1 - OK
# 0 - Instabilidades

# valores_coletados = [0, 1, 1, 1, 0, 0, 1, 1]
# resultado = 3

valores_coletados = [1, 1, 1, 1, 0, 0, 1, 1]
# resultado = 4


def verifying(array):
    maxOk = 0
    counter = 0
    for i in range(len(array)):
        if array[i] == 0:
            counter = 0
        else:
            counter += 1
            if counter > maxOk:
                maxOk = counter
    return maxOk


result = verifying(valores_coletados)
print('resultado: ', result)
