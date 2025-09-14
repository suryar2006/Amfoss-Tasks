print("Hello, World!")
print()

h=5

for i in range(h):
    for j in range(h*2-1):
        if i==h-1:
            print("*",end="")
        elif j==h-1-i or j==h-1+i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print()

try:
    f=open("input.txt","r")
    num=int(f.read().strip())
    f.close()
except:
    num=h

for i in range(num):
    for j in range(num*2-1):
        if i==num-1:
            print("*",end="")
        elif j==num-1-i or j==num-1+i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
