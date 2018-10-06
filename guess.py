import random

answer = int(random.uniform(1, 30))

num = int(input('猜猜数字：'))

if num == answer:
    print('厉害了,第一次就猜对了')
while num != answer:
    if num > answer:
        print('大了')
        num = int(input('再猜一次试试：'))
    if num < answer:
        print('小了')
        num = int(input('再猜一次：'))
    if num == answer:
        print('你赢了')
        break
