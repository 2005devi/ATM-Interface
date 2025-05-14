def reverse_num(n,re=0):
    
    if n==0:
        return re
    b=n%10
    re=re*10+b
    return reverse_num(n//10,re)
n=int(input())
print(reverse_num(n))