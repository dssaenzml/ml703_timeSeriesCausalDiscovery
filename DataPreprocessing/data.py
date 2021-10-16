import sys
import os

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path+"\\DataPreprocessing")

# sys.path.insert(0, 'DataPreprocessing')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime, timezone

from sklearn.linear_model import LinearRegression

def set_datetime(data, tz = 'Asia/Qatar', unit='s', utc=True):
    ''' 
    Change pandas conlum from seconds from epoch to datetime format.
    '''

    datetime_column = pd.to_datetime(data, unit=unit, utc=utc)
    if tz is None:
        return datetime_column

    datetime_column = datetime_column.dt.tz_convert(tz)
    return datetime_column

def detrend_ts(ts_data, **kwargs):
    ''' 
    Find trend line for a timw series and subtract it.
    '''

    X = [i for i in range(0, len(ts_data))]
    X = np.reshape(X, (len(X), 1))
    y = ts_data

    lr_model = LinearRegression(**kwargs)
    lr_model.fit(X, y)

    trend = lr_model.predict(X)

    detrended_ts_data = [y[i]-trend[i] for i in range(0, len(ts_data))]
    return detrended_ts_data

def take_diff_ts(ts_data, lag, final_ts_len):
    ''' 
    Take the difference between present value and a lagged value.
    '''
    
    temp = np.diff(ts_data, n=lag)
    ts_data = ts_data[-final_ts_len:]
    return ts_data