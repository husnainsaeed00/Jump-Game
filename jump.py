class Solution:
    def canJump(self, nums):
        max_reachable = 0
        
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            
            max_reachable = max(max_reachable, i + nums[i])
            
            if max_reachable >= len(nums) - 1:
                return True
        
        return True  # If we've iterated through the whole array successfully

# Test cases
nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]

solution = Solution()
print(solution.canJump(nums1))  # Output: True
print(solution.canJump(nums2))  # Output: False
