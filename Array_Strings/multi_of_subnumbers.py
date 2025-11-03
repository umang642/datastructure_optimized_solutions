from typing import List

class MultiOfSubNumbers:
    def get_the_multiplication(self, nums: List[int]) -> List:
        result_array = []
        pointer_j = 0

        for pointer_i in range(len(nums)):
            multiplication_result = 1

            while pointer_j < len(nums):
                if pointer_i != pointer_j:
                    multiplication_result *= nums[pointer_j]
                    pointer_j += 1
                else:
                    pointer_j += 1
                
            result_array.append(multiplication_result)
            
            # set the pointer to 0. 
            pointer_j = 0
        
        return result_array
    
    def get_more_optimized_solution(self, nums: List[int]) -> List:
        n = len(nums)
        output_arr = [1] * n

        prefix = 1
        for i in range(n):
            output_arr[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for j in range(n - 1, -1, -1):
            output_arr[j] *= suffix
            suffix *= nums[j]

        return output_arr            


if __name__ == "__main__":
    nums = [1,2,2,4]
    s = MultiOfSubNumbers()
    print(s.get_more_optimized_solution(nums=nums))
