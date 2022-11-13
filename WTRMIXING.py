# cook your dish here
for t in range(int(input())):
    a,b,x,y=map(int,input().split())
    if(a==b):
        print("YES")
    elif(a>b):
        c=a-b
        if(y>=c):
            print("YES")
        else:
            print("NO")
    else:
        c=b-a
        if(x>=c):
            print("YES")
        else:
            print("NO")
    
