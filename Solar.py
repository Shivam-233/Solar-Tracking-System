n = int(input("enter n : "))
count: 1
for i in range (n):
    c = count
    for j in range (i+1):
        print (c, end = '\t')
        c= c-1
    print()
    count=count +1+2
 
