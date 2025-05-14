def prime_num(n,i=2):
    if n<2:
        return 0
    if n%i==0 and n!=i:
        return 0
    if i*i>n:
        return 1
    return prime_num(n,i+1)
def count_primes(nums,j=0):
    if j==len(nums):
        return 0
    if prime_num(nums[j]):
        return 1+count_primes(nums,j+1)
    else:
        
        return count_primes(nums,j+1)
nums=list(map(int,input().split()))
print(count_primes(nums))