nums = input('Digite uma sequência de números separados por espaço: ')

num_list = nums.split(' ')

sum_num = 0

for num in num_list:
    if not num.isdigit():
        print(f"Erro ao somar os valores, {num} não é um número")
    else:
        sum_num += int(num)

print(f"A soma dos valore é {sum_num}")
