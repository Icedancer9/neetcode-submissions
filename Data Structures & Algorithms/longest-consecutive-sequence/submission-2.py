class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # 0 -> 1 check, if good -> 1 -> 2, if good -> 2 -> if bad -> end: start at index 1 
        # Sum of first N integers == n^2/2 + n/2 == O(N^2)

        # We can skip these redundant checks. n to m is increasing, we don't have to start from n + 1 bc it will end at m 

        # We can use additonal space to reduce time complexity. Sorting turns it into O(n log n) 
        
        # the potential largest consecutive sequence is min(n) to max(n). 
            # i is the current element in n 
        # n[i] -> store i + 1 in O(1) look up ds. set or dict 
        set_nums = set(nums)
        max_cons_seq = 0
        seen_nums = set()
        min_num = None
        for num in set_nums:
            temp_num = num
            temp_seq = 0
            if temp_num not in seen_nums:
                while temp_num + 1 in set_nums:
                    seen_nums.add(temp_num + 1)
                    temp_seq += 1
                    temp_num += 1
            max_cons_seq = max(temp_seq + 1, max_cons_seq)
        return max_cons_seq 










         
        


            
        