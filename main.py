from retweet import dothert
from time import sleep
import sys

def logtofile(logstr):
    print 'log goes ' + logstr
    print 'how about \ntail -f '+logstr
    sys.stdout = open(logstr, 'a', 0)
    # print('{0}'*10 + '\n log started at {1} \n' + '{0}'*10).\
    # format('X', str(datetime.datetime.now()))

logtofile('log')
while True:
    dothert()
    sleep(300)
