from typing import List

# get the 2 variable 1, current_sum and max sum >> compare both and if the first number is -ve just reset to 0 or current_sum went to -ve set to 0
class MaxSubArray:
    def get_max_sub_array(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            max_sum = max(current_sum, max_sum)

            if current_sum < 0:
                current_sum = 0
        
        return max_sum
    
if __name__ == '__main__':
    nums = [1,2,3,-1,2,-2,4]
    s = MaxSubArray()
    print(s.get_max_sub_array(nums=nums))
