from typing import List

class AddPlusOne:
    def get_array_with_plus_one(self, nums: List[int]) -> List:

        for last_digit in range(len(nums) - 1, -1, -1):
            nums[last_digit] += 1
            
            # if it's < 10 then return all digits
            if nums[last_digit] < 10:
                return nums
            # else replce that digit with 0
            nums[last_digit] = 0
            # return 1 with ahed of that digit. 
            return [1] + nums

if __name__ == '__main__':
    nums = [9]
    s = AddPlusOne()
    print(s.get_array_with_plus_one(nums=nums))
