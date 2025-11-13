### here we are keeping duplicate number not more than 2. 
### for e.g: [1,1,1,1,2,2,3,4,5,5] --- > [1,1,2,2,4,5,5,-,-,-,-]

from typing import List

class RemoveDuplicateFromSortedArray:
    def remove_dup_from_sorted_array(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        j = 0

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        
        return j

if __name__ == '__main__':
    nums = [1,1,1,1,2,2,3,4,5,5]
    s = RemoveDuplicateFromSortedArray()
    print(s.remove_dup_from_sorted_array(nums=nums))