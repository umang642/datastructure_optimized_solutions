from typing import List

class FindClosestNumber:
    def getClosestNumber(self, nums: List[int]) -> int:
        # get the first number as closest number 
        closest_number = nums[0]
        
        # run the loop and compare with the closest number and if it the other number is closest update the closest variable
        for number in nums:
            if abs(number) < abs(closest_number):
                closest_number = number
        
        if closest_number < 0 and abs(closest_number) in nums:
            closest_number = abs(closest_number)
        else:
            closest_number = closest_number
        
        return closest_number

if __name__ == "__main__":
    input_number = [1,-1,3,-2,-8]
    page_object = FindClosestNumber()
    print(page_object.getClosestNumber(nums=input_number))
