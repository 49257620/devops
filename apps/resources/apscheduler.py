# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
import datetime

scheduler = BlockingScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')


@register_job(scheduler, "interval", seconds=10)
def myTestJob():
    print("myTestJob auto run {}".format(datetime.datetime.now()))


register_events(scheduler)

# scheduler.start()
