# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-09-09 21:03:21
# @Last Modified by:   jerry
# @Last Modified time: 2017-09-23 17:09:41

import pandas as pd

from log_lib import log


def get_csv(filename,path=None):
    df = pd.read_csv(filename)
    return df


def pandas_apply(data):
    # Convert date from string to date times
    data['date'] = pd.to_datetime(data['date'])
    return data

def main():
    filename = 'phone_data.csv'
    df = get_csv(filename)
    data  = pandas_apply(df)
    
    log.notice(data['item'].count())
    
    log.notice(data['duration'][data['item']=='call'].sum()) # How many seconds of phone calls are recorded in total?)
    log.notice(data['month'].value_counts()) # How many entries are there for each month?)
    log.notice(data['network'].nunique()) # Number of non-null unique network entries)
    log.notice(data.groupby('month').first()) # Get the first entry for each month)
    log.notice(data.groupby('month')['duration'].sum()) # Get the sum of the durations per month)
    log.notice(data.groupby('month')['date'].count()) # Get the number of dates / entries in each month)
    log.notice(data[data['item']=='call'].groupby('network')['duration'].sum())# What is the sum of durations, for calls only, to each network)
    log.notice(data.groupby(['item','month'])['date'].count())  # How many calls, sms, and data entries are in each month?)
    log.notice(data.groupby(['month','item'])['date'].count())  # How many calls, sms, and data entries are in each month?)
    log.notice(data.groupby(['month','network_type'])['duration'].count()) # How many calls, texts, and data are sent per month, split by network_type?)
    log.notice(data.groupby('month')['duration'].sum())  # produces Pandas Series)
    log.notice(data.groupby('month')[['duration']].sum()) # Produces Pandas DataFrame)
    log.notice(data.groupby('month',as_index=False).agg({"duration":"sum"}))
    d = {"duration":"sum","network_type":"count","date":"first"}
    log.notice(data.groupby(['month','item']).agg(d))

    aggegation = {
    "duration":"sum",
    
    "date":lambda x:max(x)
    }
    log.notice(data.groupby('month').agg(aggegation))

    log.notice("."*40)
    log.notice(data.groupby(['month','item']).agg({'duration':[min,max,sum],'network_type':"count",
        "date":[min,"first","nunique"]}))

    log.notice("-"*40)
    log.notice(data.groupby('month').agg({"duration":[min,max,"mean"]}))


if __name__ == '__main__':
    main()
