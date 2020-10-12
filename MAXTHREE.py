n=int(input())
if(0<=n<=20):
 for i in range(1,n+1):
   x, y, z = [int(x) for x in input().split()]
   if(0<=y<=100000 and 0<=x<=1000000 and 0<=z<=1000000):
    if(x>y and x>z):
     print(x)
    elif(y>x and y>z):
     print(y)
    else:
      print(z)