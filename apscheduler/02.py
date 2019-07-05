# coding:utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

def aps_test():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print('你好')

scheduler = BlockingScheduler()
scheduler.add_job(func=aps_test,trigger='cron',second='*/5')
scheduler.start()
