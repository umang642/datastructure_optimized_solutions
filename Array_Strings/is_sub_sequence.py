from typing import List

class SubSequence:
    def get_sub_sequence(self, strings: List[str]) -> str:
        # find the minimum length of the string, because some time it will be flows, flo, fl too. 
        min_length = float('inf')

        for s in strings:
            if len(s) < min_length:
                min_length =  len(s)
                
        i = 0
        while i < min_length:
            for s in strings:
                if s[i] != strings[0][i]:
                    return s[:i]

            i += 1
        
        return s[:i]
    

if __name__ ==  "__main__":
    strings = ['hello', "hell", "hellow"]
    s = SubSequence()
    print(s.get_sub_sequence(strings=strings))

