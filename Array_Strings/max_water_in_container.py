from typing import List

class MaxWaterInContainer:
    def max_water_in_container(self, hights: List[int]) -> int:
        left, right = 0, len(hights) - 1
        max_area_of_water = 0

        while left < right:
            # get the area
            area = (right-left) * min(hights[left], hights[right])
            # ge the max area
            max_area_of_water = max(area, max_area_of_water)

            # check left increment and decrement 
            if hights[left] < hights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area_of_water
    
if __name__ == '__main__':
    hights = [1,7,2,5,4,7,3,6]
    s = MaxWaterInContainer()
    print(s.max_water_in_container(hights=hights))
