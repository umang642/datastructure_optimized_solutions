from typing import List

class NumberSequence:
    def get_number_sequence(self, nums: List[int]) -> List:
        i = 0 
        result_array = []
        while i < len(nums):
            start = nums[i]

            while i < len(nums) - 1 and nums[i]+1 == nums[i+1]:
                i += 1
            
            if start == nums[i]:
                result_array.append(nums[i])
            else:
                result_array.append(str(start) + '->' + str(nums[i]))
            
            i += 1
        
        return result_array

if __name__ == "__main__":
    intput_array = [0,1,3,5,6,7,8,9]
    s = NumberSequence()
    print(s.get_number_sequence(nums=intput_array))