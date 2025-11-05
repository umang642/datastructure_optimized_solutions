from typing import List
from collections import defaultdict

class GroupOfAnagram:
    def get_group_of_anagram(self, anagram_list: List[str]) -> List[str]:
        # get the dictonary of anagram 
        dict_for_anagram = defaultdict(list)
        # run the loop of each string and set the char array for assci char
        for word in anagram_list:
            count = [0]*26
            for char in word:
                count[ord(char) - ord('a')] += 1
            dict_for_anagram[tuple(count)].append(word)
        
        return dict_for_anagram.values()

if __name__ == '__main__':
    anagram_list = ['eat','ate','pat','eta','pot','tap']
    s = GroupOfAnagram()
    print(s.get_group_of_anagram(anagram_list=anagram_list))
