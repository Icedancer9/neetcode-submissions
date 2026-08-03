class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return Answer.calc_answer(nums)
         


class Answer:
    def calc_answer(nums: List[int]) -> List[int]:
        # nums = [-5, 4, 3, 2, 10]
        # left_of_n = [1, -5, -20, -60, -120]
        # right_of_n = [1, 10, (right_of_n[-1] * nums[i-1]) , 240]
        # ans = [left_of_n * right_of_n,  x, x, x,  x ]

        left_of_n = [1]
        for i in range(1, len(nums)):
            left_of_n.append(left_of_n[-1] * nums[i-1]) 
        right_of_n = [1]
        for i in range(len(nums) - 2, -1, -1):
            right_of_n.append(right_of_n[-1] * nums[i+1])
        right_of_n.reverse()
        ans = [left_of_n[i] * right_of_n[i] for i in range(len(left_of_n))]
        return ans





