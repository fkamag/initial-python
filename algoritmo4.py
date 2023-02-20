def check_sum(numbers: list, target: int):  # N = len(numbers)
    """fazer uma dupla iteração
    - para cada numero:
        - vê se tem algum outro na lista que a soma == alvo
          e o index é diferente
    Complexidade do nosso algoritmo: O(N²)
    """

    # executa N * O(N) = O(N²)
    for first_index, first_num in enumerate(numbers):
        # executa N * O(1) = O(N)
        for second_index, second_num in enumerate(numbers):
            # constante = O(1)
            if (first_index != second_index) and (
                first_num + second_num == target
            ):
                return True
    return False


def test_check_sum():
    assert check_sum([2, 2, 2, 2, 2, 2, 2], 5) is False
    assert check_sum([-1, 1, 1, 2, 3, 4], 7) is True
    assert check_sum([1, 2, 5, 8, 13, 21], 3) is True
    assert check_sum([1, 2, 5, 8, 13, 21, 21], 22) is True
    assert check_sum([4, 3], 8) is False
    assert check_sum([1, 1, 2, 4, 4], 7) is False
    assert check_sum([1, 2, 3, 4], 9) is False
    assert check_sum([1, 20, 300, 4000], 0) is False