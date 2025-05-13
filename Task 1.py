
def fun(n):
    if n < 2:
        return 1
    else:
        return n* (fun(n-1))

res=int(input('Enter a number: '))
print('Facttorial of ',res , ' is: ', fun(res))