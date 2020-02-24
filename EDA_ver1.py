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

mens_dir = 'google-cloud-ncaa-march-madness-2020-division-1-mens-tournament'
womens_dir = 'google-cloud-ncaa-march-madness-2020-division-1-womens-tournament'

def time_meter()


def log_loss(target, pred, eps=1e-15):
    p=np.clip(pred,eps, 1-eps)
    if target==1:
        return np.log(p)
    elif target==0:
        return np.log(1-p)
