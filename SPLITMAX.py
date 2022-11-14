# cook your dish here
for t in range(int(input())):
    n=int(input())
    m=998244353
    c=list(map(int,input().split()))
    #print(c)
    count=sum(c)
    print(count*(count-1) % m)
    
    
    
        
