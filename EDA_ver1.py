import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import matplotlib as mpl
from matplotlib.patches import Circle, Rectangle, Arc
import seaborn as sns
plt.style.use('seaborn-dark-palette')
mypal = plt.rcParams['axes.prop_cycle'].by_key()['color'] # Grab the color pal
import os
import gc
import time

mens_dir = 'google-cloud-ncaa-march-madness-2020-division-1-mens-tournament'
womens_dir = 'google-cloud-ncaa-march-madness-2020-division-1-womens-tournament'

#time_meter
def stop_watch(func):
    def wrapper(*args, **kargs):
        start_time=time.time()
        result=func(*args, **kargs)
        elapsed_time=time.time() - start_time
        print(f"Function:'{func.__name__}' needed {elapsed_time} sec.")
        return result
    return wrapper

def log_loss(target, pred, eps=1e-15):
    p=np.clip(pred,eps, 1-eps)
    if target==1:
        return np.log(p)
    elif target==0:
        return np.log(1-p)
