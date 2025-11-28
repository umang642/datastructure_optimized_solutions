class FindTheFirstOccuranceOfString:
    def get_first_occurance_of_string(self, string1: str, string2: str) -> int:

        # check string1 or string2 should not be None
        # check string1 should be greater than string2
        # check string2 not in string1 return -1
        # add string1 into an array
        # take the window of string2 
        # run the loop for string2 and check the widow is available then return ith position

        if not string1: return -1
        if not string2: return -1
        if string1 < string2: return -1
        if string2 not in string1: return -1

        string1_arr = []
        for i in range(len(string1)):
            string1_arr.append(string1[i])
        
        window_size = len(string2)

        for i in range(len(string1) - window_size +1):
            if ''.join(string1[i: i + window_size]) == string2:
                return i
            
        return -1

if __name__ == '__main__':
    string1 = 'cbcabcpqr'
    string2 = 'abc'
    s = FindTheFirstOccuranceOfString()
    print(s.get_first_occurance_of_string(string1=string1, string2=string2))