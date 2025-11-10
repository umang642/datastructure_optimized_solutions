"""
Here, S is the string which should be inside the T string. if not, return false

Condition checked: 
- If length of T is higher than S return False 
- If S is blank return True 
- if S have only one letter or it;s reached to end of the length check that. 

If s and t pointers are matching then only move to next or traverse t until you find. 
"""
class SubString:
    def is_sub_string(self, S: str, T: str):
        if len(T) < len(S): return False
        
        # get the window_size of the comparision.
        window_size = len(S)

        for start in range(len(T) - window_size + 1):
            if T[start:start + window_size] == S:
                return True
        
        return False

if __name__ == "__main__":
    string1 = "abc"
    string2 = "pqabc"
    s = SubString()
    print(s.is_sub_string(S=string1, T=string2))