# encoding: utf-8
# -*- coding: utf-8 -*-
# author = ‘LW’

from django.core.management import BaseCommand
from resources.apscheduler import scheduler


class Command(BaseCommand):
    def handle(self, *args, **options):
        scheduler.start()