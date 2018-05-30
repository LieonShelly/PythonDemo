import  time
import datetime
import random

string_2_struct = time.strptime("2016/05/22","%Y/%m/%d")
time.mktime(string_2_struct)
time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())
datetime.datetime.now()
datetime.date.fromtimestamp(time.time())
datetime.datetime.now()
datetime.datetime.now() + datetime.timedelta(3)
datetime.datetime.now() + datetime.timedelta(-3)
datetime.datetime.now() + datetime.timedelta(hours=3)
datetime.datetime.now() + datetime.timedelta(minutes=30)
random.random()
random.randint(1,2)
random.randrange(1,10)