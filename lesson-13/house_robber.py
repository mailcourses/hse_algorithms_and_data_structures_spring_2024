#! /usr/bin/env python3

#         0 1 2 3 4
# nums = [1,2,3,1]
#                 i
# dp   = [1,2,4,4]
def rob(nums):
    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])

    return dp[-1]

if __name__ == "__main__":
    assert rob([2,7,9,3,1]) == 12
    assert rob([1,2,3,1]) == 4
