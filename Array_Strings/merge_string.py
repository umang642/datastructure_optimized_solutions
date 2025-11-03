class MergeString:
    def get_final_merged_string(self, input_string: str, input_string2: str) -> str:
        A, B = len(input_string), len(input_string2) # length for loop
        a, b = 0, 0 # these are the index
        merging_string = [] # store the results here 
        word1, word2 = input_string, input_string2

        while a < A and b < B:
            merging_string.append(word1[a])
            a += 1
            merging_string.append(word2[b])
            b += 1
        
        while a < A:
            merging_string.append(word1[a])
            a += 1
        
        while b < B:
            merging_string.append(word2[b])
            b += 1
        
        return ''.join(merging_string)

if __name__ == '__main__':
    input_string = 'abc'
    input_string2 = 'pqr'
    s = MergeString()
    print(s.get_final_merged_string(input_string=input_string, input_string2=input_string2))

### output will be "apbqcr"