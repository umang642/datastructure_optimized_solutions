from typing import List

class FindNumberInTwoDMatrix:
    def is_number_found_in_matrix(self, matrix: List[List[int]], target: int) -> bool:
        m_row = len(matrix)
        n_column = len(matrix[0])
        total_number = m_row * n_column
        left = 0
        right = total_number - 1

        while left <= right:
            mid = (left + right) // 2
            i = mid // n_column
            j = mid % n_column

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid[i][j] + 1
            else: 
                right = mid[i][j] - 1

        return False

if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    target = 13
    s = FindNumberInTwoDMatrix()
    print(s.is_number_found_in_matrix(matrix=matrix, target=target))
