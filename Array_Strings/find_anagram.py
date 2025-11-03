class Solution:
    def hasAnagram(self, string_1: str, string_2: str):
        return sorted(string_1) == sorted(string_2)
    
    def hasAnagramWithOutSorted(self, string_1: str, string_2: str) -> bool:
        if len(string_1) != len(string_2):
            return False
        
        # create a dictonary to store the anagram. 
        dict_string_1 = {}    

        for ch in string_1:
            dict_string_1[ch] = dict_string_1.get(ch, 0) + 1
        
        for ch in string_2:
            if ch not in dict_string_1:
                return False
            
            dict_string_1[ch] -= 1

            if dict_string_1[ch] == 0:
                del dict_string_1[ch]
        
        return len(dict_string_1) == 0

if __name__ == "__main__":
    string_1 = "xxx"
    string_2 = "xax"
    s = Solution()
    print(s.hasAnagramWithOutSorted(string_1=string_1, string_2=string_2))