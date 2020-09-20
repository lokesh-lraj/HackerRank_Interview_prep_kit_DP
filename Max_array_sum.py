"""
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.

For example, given an array arr = [-2, 1, 3, -4, 5] we have the following possible subsets: 
Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8

Our maximum subset sum is 8.

Input Format

The first line contains an integer,n
.
The second line contains n space-separated integers arr[i]. 

constraints:
  1 <= n <= 10^5
  -10^4 <= arr[i] <= 10^4

Output Format

Return the maximum sum described in the statement.

Sample Input 0

5
3 7 4 6 5

Sample Output 0

13
    ---------------------------
Sample Input 1

5
2 1 5 8 4

Sample Output 1

11
'''
def maxSubsetSum(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if n == 2:
        return arr[1]
    dp = [0]*n
    dp[0] = arr[0]
    dp[1] = max(arr[1], arr[0])
    for i in range(2,n):
        dp[i] = max(arr[i]+dp[i-2], dp[i-1], arr[i])
    return dp[-1]
