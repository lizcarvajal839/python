#function Fibonacci Series
def fib(n):
    first=0
    second=1
    #cases to consider
    if n<1:
        return -1
    if n==1:
        return first
    if n==2: 
        return second
    #stars at 2 because i=0 => 0 i =1 =>1 
    for i in range(2,n):
        result=first+second
        first=second
        second=result
    return result

print(fib(7))