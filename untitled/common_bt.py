import pandas as pd
import numpy as np

COMMISSION_FEE_RATE = 0.0003  # 类属性

# input data sample as a dictionary
Input = {"symbol": "A.DCE", 
         "OT" : "09:00",      # order time 
         "rollover rule name" : "OI",  # rollover rule name
         "date": ["20160101", "20220930"]}    # date range

def func_ret_tov_df(weight, close_df):
    weight = weight.fillna(0)
    weight1 = weight.loc[weight.index[0]]
    weight_diff = weight.diff()
    weight_diff.loc[weight.index[0]] = weight1
    tov_df = weight_diff.fillna(0).abs()
    ret_df = (weight * close_df.pct_change(axis=0).shift(-1)).shift(1).fillna(0)
    ret_net_vec = (ret_df - tov_df * COMMISSION_FEE_RATE).sum(axis=1)
    return ret_df, tov_df, ret_net_vec

def func_summary(weight, close_df, freq = 52):
    ret_df, tov_df, ret_net_vec = func_ret_tov_df(weight, close_df)
    
    # Trunover (float)
    TOV = tov_df.mean(axis=1).mean()
    
    r = pd.Series(ret_net_vec)
    Mean = np.mean(r)*freq
    Volatility = np.std(r)*np.sqrt(freq)
    SR = Mean/Volatility
    
    #MDD
    r_cumsum = r.cumsum()
    r_cummax = r_cumsum.cummax()
    MDD = max((r_cummax - r_cumsum)/r_cummax)
    
    return TOV, Mean, Volatility, SR, MDD



class backTest(object):
    
    # a function to get clean data
    


    