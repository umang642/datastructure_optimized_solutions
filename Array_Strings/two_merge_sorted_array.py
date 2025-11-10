from typing import List

class TwoMergedSortedArray:
    def get_the_sorted_array(self, nums1: List[int], nums2: List[int], m: int, n: int) -> List:
        # get three pointers x should be set at len(m) y should be set at len(n) and Z at the m + n
        x, y = m - 1, n - 1

        for z in range(m + n - 1, -1, -1):
            # if x is empty array, still continue add the y at the end
            if x < 0:
                nums1[z] = nums2[y]
                y -= 1
            # if y is empty array
            elif y < 0:
                break
            # if x > y then push back x to zth location
            elif nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x -= 1
            # if x and y same keep it at the current zth location
            else:
                nums1[z] = nums2[y]
                y -= 1
        
        return nums1

if __name__ == '__main__':
    num1 = [1,2,3,4,0,0,0]
    num2 = [3,5,6]
    s = TwoMergedSortedArray()
    print(s.get_the_sorted_array(nums1=num1, nums2=num2, m=4, n=3))