# import math
# import os
# import random
# import re
# import sys


if __name__ == '__main__':

    arr = [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5],
           [-1, -1, -1, -2, -3, -4], [-1, -9, -2, -4, -4, -5],
           [-7, -3, -3, -2, -9, -9], [-1, -3, -1, -2, -4, -5]]

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    max_sum = -1000
    for i in range(len(arr)-2):
        cont = 0
        for j in range(len(arr)-2):
            cont = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1]
            + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if cont > max_sum:
                max_sum = cont
    print(max_sum)
