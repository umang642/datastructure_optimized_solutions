class ValidatePalindrom:
    def is_it_palindrom_or_not(self, chars: str) -> bool:
        i = 0
        j = len(chars) - 1

        while i < j:
            if chars[i] == chars[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    chars = 'aba'
    s = ValidatePalindrom()
    print(s.is_it_palindrom_or_not(chars=chars))
