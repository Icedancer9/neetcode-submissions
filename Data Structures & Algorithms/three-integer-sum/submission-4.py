class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return TrueSolution.threeSumCalculation(nums)


class TrueSolution:
    def threeSumCalculation(nums: List[int]) -> List[List[int]]:

        nums.sort()

        # [-4, -1, -1, 0 1, 2]
        # Trivial solution is O(N^3) ~= (O(I * ((I - 1)(I - 2))))

        # We want to get it down to n^2 or n^2 + n log n 
        
            # sort this list 
            # turn into 2 sum problem 
        
        # Now we are just looking for one number that two other numbers sum to the opposite of 
        i = 0
        ans = []
        while i < len(nums): 
            j = i + 1         
            k = len(nums) - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum < 0:
                    j += 1
                elif three_sum > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < len(nums) and nums[j] == nums[j - 1]:
                        j += 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return ans 


                
                






            