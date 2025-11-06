from typing import List

# List: [10,9,2,5,3,7,101,18]

class FindLongestSequence:
    def get_longest_sequence_number(self, nums: List[int]) -> int:
        result_array = []
        next_number = float('inf')

        # first get the 1st smallest number in list 
        i = 0
        while nums[i] < next_number:
            next_number = nums[i]
            i += 1
        
        result_array.append(next_number)
        loop_pointer = nums.index(next_number)

        # starting point for loop will be smallest number
        for j in range (loop_pointer+1, len(nums)):
            if nums[j] > next_number:
                next_number = nums[j]
                result_array.append(nums[j])
        
        return len(result_array)


if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    s = FindLongestSequence()
    print(s.get_longest_sequence_number(nums=nums))
        