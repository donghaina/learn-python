num = 0
while num < 10:
    print("The num is ",num)
    num = num + 1;
print('----------------')

num = 0
while num<10:
    num += 1
    if num % 2 == 1:
        continue
    print num
    
print('----------------')

num = 0
while num<10:
    print num
    num+=1
    if num>5:
        break
        