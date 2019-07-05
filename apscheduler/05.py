# coding:utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log1.txt',
                    filemode='a')


def aps_test(x):
    print(1/0)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)

scheduler = BlockingScheduler()
scheduler.add_job(func=aps_test, args=('定时任务',), trigger='cron', second='*/5')
scheduler._logger = logging
scheduler.start()
