# Appraoch 1
#Approch of getting missing numbers in an array by using N natural numbers Summation Method....

# def getting_missing_summation(a):
#     n = a[-1]
#     sum1=0
#     total=n*(n+1)//2
#     sum1=sum(a)
#     print(total - sum1)
      
# a = [1,2,3,5,6,7,8,9] 
# getting_missing_summation(a)




# Approach 2
# Approach of getting missing number using xor method. 
#     - first getting xor of all element of an array
#     - second getting xor of index including missing number index 
#     - finally do xor of first and xor of second

def get_missing_number_xor(n,a):
    xor1 = a[0]
    for index in range(1,n):
        xor1 ^= a[index]
        
    xor2 = 0 
    for index in range(1,n+2):
        xor2 ^= index 
        
    print(xor1^xor2)
    
a = [1,2,3,5,6,7,8,9] 
get_missing_number_xor(len(a),a)

    