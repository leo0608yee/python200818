import random
A=random.randrange(1,20)
i=1
while i<6:
    B=int(input("請輸入數字"))
    if B>A:
        print('太大了喔')
    if B<A:
        print('太小了喔')
    if B==A:
        print("恭喜第",i,"次答對")
        break
    i=i+1 
    
