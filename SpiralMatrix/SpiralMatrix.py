class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            ans += matrix[0]
            matrix.pop(0)
            [r.reverse() for r in matrix]
            matrix = [list(r) for r in zip(*matrix)]
        return ans