class ClimbingStairs:

    def climbing_stairs(self, num: int) -> int:

        def dfs(i):
            if i >= num:
                return i == num
            
            return dfs(1 + i) + dfs(2 + i)
        
        return dfs(0)
    

if __name__ == '__main__':
    num = 10
    s = ClimbingStairs()
    print(s.climbing_stairs(num=num))