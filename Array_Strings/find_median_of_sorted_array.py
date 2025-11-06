from typing import List

class FindMedianOfSortedArray:
    def get_the_median_number_array(self, array_1: List[int], array_2: List[int]) -> int:
        # Combine both array 
        for num in array_2:
            array_1.append(num)

        # sort the array_1
        array_1 = sorted(array_1)
        print('sorted array', array_1)

        # get the center of array 
        center_array_1 = len(array_1) // 2

        # check the mod is 0 then it even >> find the center of even or center will be median number
        if len(array_1) % 2 == 0:
            median = (array_1[center_array_1 - 1] + array_1[center_array_1]) / 2
        else:
            median = array_1[center_array_1]
        
        return median
    
if __name__ == '__main__':
    array_1 = [1,2,3]
    array_2 = [2,3,4]
    s = FindMedianOfSortedArray()
    print(s.get_the_median_number_array(array_1, array_2))
