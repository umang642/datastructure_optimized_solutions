class GetLongestSubString:
    def get_longest_sub_string(self, s: str) -> int:
        n = len(s)

        # Go to longest to smallest
        for L in range(n - 1, 0, -1):
            seen = set()
            # create substring and add it to set
            for i in range(n - L + 1):
                sub_string = s[i: i+L]
                if sub_string in seen:
                    return L
                seen.add(sub_string)
        
        return 0
    
if __name__ == '__main__':
    word = 'aabaabaa'
    s = GetLongestSubString()
    print(s.get_longest_sub_string(s = word))
