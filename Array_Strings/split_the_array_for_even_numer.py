from typing import List

class SplitTheArray:
    def is_split_is_possible(self, nums: List[int]) -> bool:

        dict_for_nums = {}
        for num in nums:
            dict_for_nums[num] = dict_for_nums.get(num, 0) + 1
        
        for key, _ in dict_for_nums.items():
            if dict_for_nums[key] > 2:
                return False
        
        return True

if __name__ == '__main__':
    nums = [1,1,1,1]
    s = SplitTheArray()
    print(s.is_split_is_possible(nums=nums))
