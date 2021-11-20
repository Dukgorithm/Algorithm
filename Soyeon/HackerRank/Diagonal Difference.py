def diagonalDifference(arr):
    left_cross, right_cross = 0, 0
    for i in range(len(arr)):
        left_cross += arr[i][i]
        right_cross += arr[i][len(arr)-i-1]
    return abs(left_cross - right_cross)
        