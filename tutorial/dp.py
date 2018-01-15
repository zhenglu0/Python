# -*- coding: utf-8 -*- 

# http://www.cppblog.com/xiaoyisnail/archive/2009/09/18/96638.html

# 题目是这样的：一个100层的大厦，你手中有两个相同的玻璃球。从这个大厦的某一层扔下
# 就会碎，用你手中的这两个玻璃球，找出一个最优的策略，来得知那个临界层面。
# 这里的最优策略指的是在这种策略下无论哪个临界层面在第几层，测试的次数最少。
# 设F(n,k)为用k个玻璃球来测试n层大厦的临界层的最少次数，状态转移方程如下：
# F(n,k)=min{max{F(r,k-1), F(n-r,k)}+1, 1<=r<=n}
# 边界条件:F(n,1)=n-1, F(1,k)=F(0,k)=0
# 状态转移方程可以这样来考虑，假设在n层楼中的第r层抛一次(对应方程中的"+1")，会有两种情况发生：
# (1)玻璃球碎，说明在第1到第r层楼中必有一层为临界层，问题转化为一个子问题：求F(r,k-1)
# (2)玻璃球不碎，说明临界层在第r+1层到第n层这n-r层楼中，问题转化为子问题:求F(n-r,k)
# 因为考虑的是最坏情况下抛球策略的所需测试次数的最小值，所以取这两种情况中的较大值，并遍历每一个可能的r，取其最小值即得到F(n,k)。

def dp(n, k):
    if k < 1 or n < 1:
        return -1

    if k == 1:
        return n-1
    if n == 1:
        return 0

    F = [[0] * (k+1) for _ in xrange(n+1)]

    # zero or first floor
    # F(1,k) = F(0,k) = 0
    for i in xrange(0, k+1):
        F[1][i] = F[0][i] = 0

    # one ball to test
    # F(n,1) = n-1
    for i in xrange(1, n+1):
        F[i][1] = i-1

    # Transition Function:
    # F(n,k)=min{max{F(r,k-1), F(n-r,k)}+1, 1<=r<=n}
    for j in xrange(2, k+1):
        for i in xrange(2, n+1):
            imin = float('inf')
            for r in xrange(1, i+1):
                imin = min(imin, max(F[r][j-1], F[i-r][j]) + 1)
            F[i][j] = imin

    return F[n][k]

print dp(5, 2)
print dp(10, 2)
print dp(100, 2)
print dp(300, 3)
