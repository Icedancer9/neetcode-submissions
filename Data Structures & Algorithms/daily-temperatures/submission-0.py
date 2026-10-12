class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        ans = [0] * len(temperatures)
        for i,v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                popped_val,popped_ind = stack.pop()
                ans[popped_ind] = i - popped_ind
            stack.append((v,i))
        return ans 



        