# Asked this in Roblox for Sr. SDET role.

from typing import List

class FindRepeatedMatrix:
    def find_repeated_numers_in_matrix(self, matrix: List[List[int]]) -> List[List]:
        m = len(matrix)
        n = len(matrix[0])

        result_array = []
        for i in range(m):
            row_dict = {}
            
            for num in matrix[i]:
                row_dict[num] = row_dict.get(num, 0) + 1
            
            for num in row_dict:
                if row_dict[num] >= 3:
                    result_array.append([num, 3])
        
        # for cloumn
        for j in range(n):
            row_dict = {}
            for i in range(m):
                num = matrix[i][j]
                row_dict[num] = row_dict.get(num, 0) + 1
            
            for num in row_dict:
                if row_dict[num] >= 3:
                    result_array.append([num, 3])

        return result_array

if __name__ == '__main__':
    matrix = [[1,2,3,3],[4,7,7,3],[7,7,7,3]]
    s = FindRepeatedMatrix()
    print(s.find_repeated_numers_in_matrix(matrix=matrix))


            