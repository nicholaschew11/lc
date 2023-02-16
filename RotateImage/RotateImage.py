class Solution:

    # tranpose and reverse each row to swap columns

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                temp = matrix[j][i]
                matrix[j][i] = matrix[n - i - 1][j]
                matrix[n - i - 1][j] = matrix[n - j - 1][n - i - 1]
                matrix[n - j - 1][n - i - 1] = matrix[i][n - j - 1]
                matrix[i][n - j - 1] = temp


    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        return matrix