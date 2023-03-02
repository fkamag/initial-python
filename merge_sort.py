def merge_sort(array, start=0, end=None):
    if end is None:
        end = len(array)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)
        merge(array, start, mid, end)
    return array


def merge(array, start, mid, end):
    left = array[start:mid]  # indexando a lista da esquerda
    right = array[mid:end]  # indexando a lista da direita

    left_index, right_index = 0, 0  # as duas listas começarão do início

    for general_index in range(start, end):
        if left_index >= len(left):
            array[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            array[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            array[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            array[general_index] = right[right_index]
            right_index = right_index + 1


def get_array(string):
    array = []
    for i in range(len(string)):
        array.append(string[i].lower())
    return array


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    first_array = get_array(first_string)
    second_array = get_array(second_string)
    first_sorted = merge_sort(first_array, 0, len(first_array))
    second_sorted = merge_sort(second_array, 0, len(second_array))
    if first_sorted == second_sorted:
        return True
    return False


# numbers = [6, 5, 3, 1, 8, 7, 2, 4]
# array1 = ['b', 'r', 'a', 's', 'i', 'l']
# array2 = ['s', 'i', 'l', 'b', 'r', 'a']
# merge_sort(numbers, 0, len(numbers))
# one = merge_sort(array1, 0, len(array1))
# two = merge_sort(array2, 0, len(array2))
# print(numbers)
# print(array1)
# print(array2)
# print(one)
# print(two)

# if one == two:
#     print('true')
# else:
#     print('false')

# result_array = get_array('Brasil')
# print(result_array)

print(is_anagram('muro', 'rumo'))
