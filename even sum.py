def even_sum(x,i=0):
    if i==len(a):
        return 0
    if a[i]%2==0:
        return a[i]+even_sum(a,i+1)
    else:
        return even_sum(a,i+1)
a=list(map(int,input().split()))
print(even_sum(a))