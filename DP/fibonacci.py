
# find nth fibonacci series using DP 

def fibo(n,dp):

	if dp[n] !=-1:
		return dp[n]

	if n==0:

		return 0

	if n==1 or n==2:
		return 1

	dp[n] = fibo(n-1,dp) + fibo(n-2,dp)

	return dp[n]


n = int(input())
dp = [-1] * (n)

nth_num = fibo(n-1,dp)

print(nth_num)