from typing import List

# nums: [1,1,2,2,2,3,3,3,3,4,4]

class MostRepeatedNumber:
    def get_most_repeated_number_lists(self, nums: List[int], k: int) -> List:

        dict_for_num = {}
        number_of_time_repeate = []
        result_array = []

        # Add first to the dictonary
        for num in nums:
            dict_for_num[num] = dict_for_num.get(num, 0) + 1

        # get the pair of number and number of time repeate in to array
        for dic_key, dic_value in dict_for_num.items():
            number_of_time_repeate.append([dic_value, dic_key])
        
        # sort the array for further check
        number_of_time_repeate.sort()

        # pull the number based on K and store in result array.
        while len(result_array) < k:
            result_array.append(number_of_time_repeate.pop()[1])
        
        return result_array

    def most_repeated_char(self, chars: str, k: int) -> str:
        dict_for_str = {}
        repeated_str_array = []

        for char in chars:
            dict_for_str[char] = dict_for_str.get(char, 0) + 1
        
        for char_key, char_value in dict_for_str.items():
            repeated_str_array.append([char_value,char_key])
        
        repeated_str_array.sort()

        result_array = []
        while len(result_array) < k:
            result_array.append(repeated_str_array.pop()[1])
        
        return result_array
        
    
if __name__ == '__main__':
    nums = [1,1,2,2,2,3,3,3,3,4,4]
    chars = 'aasdddsssccvbbbbeeeesssddddsqqq'
    k = 2
    s = MostRepeatedNumber()
    print(s.most_repeated_char(chars=chars, k=k))
    print(s.get_most_repeated_number_lists(nums=nums, k=k))

