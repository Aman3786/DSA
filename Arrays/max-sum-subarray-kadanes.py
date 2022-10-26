# Python Project to find maximum sum subarray -> Brute Force to Optimized (Kadane's algo) approach 



arr = [1,-10,5,2,-1,7]



# Brute Force approach

# TC - O(n^2)

# SC - O(1)





maxsum = 0

for i in range(len(arr)):

    summ = 0

    for j in range(i,len(arr)):

        summ += arr[j]

        maxsum = max(maxsum,summ)

        

print(maxsum)







# Optimize approach (Kadane's Algo)

# TC - O(n)

# SC - O(1)



maxsum = 0

currsum = 0



for i in range(len(arr)):

    currsum = max(arr[i], currsum+arr[i])

    maxsum = max(maxsum,currsum)

    

    

print(maxsum)



        
