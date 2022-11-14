# cook your dish here
fact={}
fact[1]=1
m=1000000007
for i in range(2,1000001):
    fact[i]=(fact[i-1]*i)%m
for t in range(int(input())):
    n=int(input())
    array=list(map(int,input().split()))
    sums=0 
    for i in array:
        sums+=fact[i]
    print(sums%m)

