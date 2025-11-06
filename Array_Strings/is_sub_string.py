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
        s_pointer = 0
        if len(S) == 0: return True
        if S > T: return False

        for t_pointer in range(len(T)):
            if T[t_pointer] == S[s_pointer]:
                if s_pointer == len(S) - 1:
                    return True
                s_pointer += 1
        
        return False

if __name__ == "__main__":
    string1 = "abc"
    string2 = "pqabc"
    s = SubString()
    print(s.is_sub_string(S=string1, T=string2))