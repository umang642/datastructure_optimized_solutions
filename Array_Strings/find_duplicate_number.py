from typing import List

class Solution:
    def hasDuplicate (self, num: List[int]) -> bool: 
        for pointer in range(len(num)):
            for number in range(pointer + 1, len(num)):
                if num[pointer] == num[number]:
                    return True
        return False

    def has_duplicate_with_set (self, num: List[int]) -> bool:
        return len(num) != len(set(num))
    
    def has_duplicate_with_dict (self, nums: List[int]) -> bool:
        number_dict = {}
        for num in nums:
            number_dict[num] = number_dict.get(num, 0) + 1
            if number_dict[num] > 1:
                return True
        return False
    

if __name__ == "__main__":
    num = [1,2,3,3]
    s = Solution()
    print(s.has_duplicate_with_dict(num))
