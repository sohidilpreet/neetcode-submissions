class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = (len(matrix[0]) * len(matrix)) - 1
        while start <= end:
            middle = (start + end) // 2
            middle_row = middle // len(matrix[0])
            row_middle_element = middle % len(matrix[0])
            element = matrix[middle_row][row_middle_element]
            if element == target:
                return True
            elif element < target:
                start = middle + 1
            else:
                end = middle - 1
        return False