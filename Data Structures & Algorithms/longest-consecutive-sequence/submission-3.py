class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Check if a number is the start of a sequence. A number i is the start of a sequence if i - 1 not in set(n)
        # Edge cases: nums == [] -> max_seq == 0
        set_nums = set(nums)
        max_seq = 0

        for num in set_nums:

            if num - 1 not in set_nums: # num is a potential sequence starter 
                temp_seq = 1
                temp_num = num
                while temp_num + 1 in set_nums:
                    temp_seq += 1
                    temp_num += 1
                max_seq = max(max_seq, temp_seq)
                
        return max_seq 












         
        


            
        