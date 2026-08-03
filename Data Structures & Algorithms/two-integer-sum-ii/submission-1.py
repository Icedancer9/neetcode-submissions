class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return TwoSum.calculateTwoSum(numbers, target)


class TwoSum:
    def calculateTwoSum(numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        # [1, 1, 2, 3] target = 4
        # [1,3][1,3]
        # cannot use the same indicies
        while p1 < p2:
            if numbers[p1] + numbers[p2] > target:
                p2 -= 1
            elif numbers[p1] + numbers[p2] < target:
                p1 += 1
            else:
                return [p1 + 1, p2 + 1]
        return [p1 + 1, p2 + 1] 


        

            


