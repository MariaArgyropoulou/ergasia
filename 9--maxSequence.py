num = input("What's your number string? ") 
if num=="":
    raise SystemExit
res1= num.find('[')
res2= num.find(']')
if (res1!=-1) and (res2!=-1):
    num=num[1:len(num)-1]
elif (res1!=-1) or (res2!=-1):
    print("wrong input")
    raise SystemExit
num=num.split(',')
num = [int(i) for i in num]
meg=-10**256
print(num)
for i in range (len(num)+1):
    for k in range (i+1,len(num)+1):
        a= sum(num[i:k])
        if a>=meg:
            meg=a
            arxh=i
            plithos = k
print (meg)
#print (arxh,plithos)
print (num[arxh:plithos])
