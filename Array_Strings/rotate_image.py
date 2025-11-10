from typing import List

class RotateImage:
    def rotate_image(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Transpoing the matrix first
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reflact the matrix after that
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n -j -1] = matrix[i][n -j -1], matrix[i][j]
        
        print(matrix)

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s = RotateImage()
    s.rotate_image(matrix=matrix)


