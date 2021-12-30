n=int(input("소수 몇개를 출력할까요? "))
cnt=0
i=0
while cnt!=n:
    result=True
    if i<2:
        result=False
    else:
        for j in range(2,i):
            if i%j==0:
                result=False
    if result==True:
        cnt+=1
        print(i, end=" ")
    i+=1   
        