def qwer(t,n,m):
    if (t==1):
        return True
    if(t<1):
        return False
    return qwer(t-n,n,m) or qwer(t-m,n,m)
def count_steps(t,n,m,steps=0):
    if t == 1:
        return steps
    if t < 1:
        return float('inf')  
    return min(count_steps(t - n, n, m, steps + 1), count_steps(t - m, n, m, steps + 1))
    
t=20
n=3
m=5
print(qwer(t,n,m))
print(count_steps(t,n,m))