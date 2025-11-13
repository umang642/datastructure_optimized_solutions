from typing import List

# List: [20,1,3,10,12,4,5,6,2]

class LongestConsicutiveRequest:
    def get_length_of_longest_consicutive_sequence(self, nums: List[int]) -> int:

        result_length = 0
        sorted_and_removed_dup = set(nums)

        for num in nums:
            i = num
            length = 0
            while i in sorted_and_removed_dup:
                i += 1
                length += 1
            
            result_length = max(result_length, length)
        
        return result_length

    def another_way_to_find(self, nums: List[int]) -> int:
        max_length = 0
        length = 1
        nums = sorted(nums)

        for i in range (len(nums) - 1):
            j = i + 1

            if nums[j] == nums[i] + 1:
                length += 1
                max_length = max(max_length, length)
        
        return max_length

if __name__ == '__main__':
    nums = [20,1,1,3,10,12,4,5,6,2]
    s = LongestConsicutiveRequest()
    print(s.another_way_to_find(nums=nums))