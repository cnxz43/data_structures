# -*conding:utf-8*-



'''
打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
'''
def rob(nums):
    if nums == []: return 0
    if len(nums)<=2:
        return max(nums)
    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[:2])
    for i in range(2,len(nums)):
        dp[i] = max(dp[i-1],dp[i-2] + nums[i])
        print(dp)
    return dp[-1]

if __name__=="__main__":
    print(rob([2,1,1,2]))