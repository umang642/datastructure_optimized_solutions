from typing import List

class BinarySearch:
    def get_the_binary_search_result(self, nums: List[int], target: int) -> bool:
        # get the Left
        left = 0
        # get the Right 
        right = len(nums) - 1
        
        # while loop until L <= R 
        while left <= right:
            # get the Middle 
            middle = (left + right) // 2 # M = L + ((R - L) // 2)
            
            # if middle == target; thats the number 
            if middle == target:
                return True
            # if the middle < target; L = m + 1
            if middle < target:
                left = middle + 1
            # if the middle > target; R = m - 1
            if middle > target:
                right = middle - 1
        
        return False

if __name__ == "__main__":
    nums = [0,1,2,3,4,5,6,7]
    s = BinarySearch()
    print(s.get_the_binary_search_result(nums=nums, target=9))
