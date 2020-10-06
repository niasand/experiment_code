#coding: utf-8
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

from log_lib import log


def frame():
    data = {'state':['hubei','sichuan','guangzhou'],'year':[2015,2016,2017],'pop':[6,7,8]}
    frame = DataFrame(data)
    log.notice(frame)

    log.notice(DataFrame(data,columns=['year','state','pop','debt']))
    log.notice(frame.columns)
    log.notice(frame['state'])
    log.notice(frame['pop'])
    log.notice(frame['year'])

    frame['debt'] = 16.5
    log.notice(frame)

    frame['debt'] = np.arange(3.)
    log.notice(frame)

    frame2 = DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three'])
    log.notice(frame2)
    val = Series([-1.2,-1.3,-1.4],index=['two','three','one'])
    frame2['debt'] = val
    log.notice(frame2)

    frame2['eastern'] = frame2.state == 'hubei'
    log.notice(frame2)
    log.notice(frame2.index)

def frame3():
    pop = {'hubei':{2001:2.4,2002:2.5}, "guangdong":{2000:2.6,2001:2.7}}
    frame3 = DataFrame(pop)
    log.notice(frame3)
    log.notice(frame3.T)
    log.notice(DataFrame(pop,index=[2001,2000,2002]))

    pdata = {'hubei':frame3['hubei'][:-2],'guangdong':frame3['guangdong'][:-2]}
    log.notice(pdata)


if __name__ == '__main__':
    frame3()
