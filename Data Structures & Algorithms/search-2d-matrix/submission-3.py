class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        row_elements = len(matrix[0])
        end = (row_elements * len(matrix)) - 1
        while start <= end:
            middle = (start + end) // 2
            middle_row = middle // row_elements
            row_middle_element = middle % row_elements
            element = matrix[middle_row][row_middle_element]
            if element == target:
                return True
            elif element < target:
                start = middle + 1
            else:
                end = middle - 1
        return False