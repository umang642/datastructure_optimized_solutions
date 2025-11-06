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


if __name__ == '__main__':
    nums = [20,1,3,10,12,4,5,6,2]
    s = LongestConsicutiveRequest()
    print(s.get_length_of_longest_consicutive_sequence(nums=nums))