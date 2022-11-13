# cook your dish here
from collections import Counter
for t in range(int(input())):
    n=int(input())
    s=input()
    flag=True
    if(n%2!=0):
        flag=False
        print("NO")
    else:
        count=Counter(s)
        #print(count)
        for i in count:
            if(count[i]%2!=0):
        
                print("NO")
                flag=False
                break
    if(flag==True):
        print("YES")
            
             
                