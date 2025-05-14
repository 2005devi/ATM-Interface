def qwer(x):
    if x <= 1:
        return x
    return qwer(x-1) + qwer(x-2)
b = qwer(5)
print(b)
