import time

# 输出时间戳
print(time.localtime(time.time()))
# 输出年月日时分秒
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(time.strftime('%A', time.localtime()))
print(time.strftime('%B', time.localtime()))
print(time.strftime('%c', time.localtime()))
