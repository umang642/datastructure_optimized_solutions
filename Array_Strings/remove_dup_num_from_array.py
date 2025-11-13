from typing import List

class RemoveDupFromArray:
    def remove_dup_from_array(self, nums: List[int]) -> List[int]:

        result_array = ['-']*len(nums)
        # dict_for_unique_array = {}
        setts = set()

        # for num in nums:
        #     dict_for_unique_array[num] = dict_for_unique_array.get(num, 0) + 1

        for num in nums:
            setts.add(num)
    
        array_position = 0
        for num in setts:
            result_array[array_position] = num
            array_position += 1
        
        return result_array

if __name__ == '__main__':
    nums = [1,1,2,2,3,4,4,5,5,6,6,6]
    s = RemoveDupFromArray()
    print(s.remove_dup_from_array(nums=nums))
