# Jump Game
## Problem Description
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Write a function canJump(nums) that returns True if you can reach the last index of the array using the jump lengths specified by each element, or False otherwise.

## Examples
### Example 1:

Input: nums = [2, 3, 1, 1, 4]
Output: True
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
### Example 2:

Input: nums = [3, 2, 1, 0, 4]
Output: False
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
Approach
This problem can be solved using a greedy approach. The idea is to iterate through the array while keeping track of the maximum reachable position. If at any point the current index surpasses the maximum reachable position, then it's not possible to proceed further, and the function should return False. Otherwise, if the loop successfully reaches the end of the array, it's possible to reach the last index, and the function should return True.

The algorithm's time complexity is O(n), where n is the length of the input array nums.

### How to Use
Clone or download this repository to your local machine.

Navigate to the repository's directory.

Open a terminal and run the Python script:
jump.py
This will execute the provided test cases and print the results.

Further Notes
The solution has been implemented in Python.
This problem is a classic example of dynamic programming and greedy algorithm.
The canJump function is encapsulated within the Solution class for better organization.
