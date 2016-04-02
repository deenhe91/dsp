[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

import nsfg
import thinkstats2 as ts
import thinkplot
import numpy as np

preg = nsfg.ReadFemPreg()

live = preg[preg.outcome == 1]


wgt_hist = ts.Hist(live.birthwgt_lb, label = 'birthwgt_lb')
thinkplot.Hist(wgt_hist)
thinkplot.Show(xlabel = 'pounds', ylabel = 'frequency', axis = [4.5, 11, 0, 3500])


preglen_hist = ts.Hist(live.prglngth, label = 'preglength')
thinkplot.Hist(preglen_hist)
thinkplot.Show(xlabel = 'weeks', axis = [27, 46, 0, 5000], ylabel = 'frequency')


#clean data
def CleanFemPreg(df):
    df.agepreg /= 100.0
    
    na_vals = [97, 98, 99]
    df.birthwgt_lb.replace(na_vals, np.nan, inplace=True)
    df.birthwgt_oz.replace(na_vals, np.nan, inplace=True)
    
    df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz/16.0
    
#live births
live = preg[preg.outcome == 1]

#First child vs nonfirst 
First = live[live.birthord == 1]
Others = live[live.birthord != 1]
# live.we > ... && live.we < ...
#rel_weights_first = First[First.totalwgt_lb > 4.5 and First.totalwgt_lb < 12]


First_hist = ts.Hist(First.totalwgt_lb)
Others_hist = ts.Hist(Others.totalwgt_lb)

width = 0.10
thinkplot.PrePlot(2)
thinkplot.Hist(First_hist, align = 'right', width = width)
thinkplot.Hist(Others_hist, align = 'left', width = width)
thinkplot.Show(xlabel = 'pounds', ylabel = 'frequency')

import math

def CohenEffectSize(sample1, sample2):
    print('Mean')
    print('First: ' + str(sample1.mean()))
    print('Other: ' + str(sample2.mean()))
    
    print('Variance')
    print('First: ' + str(sample1.var()))
    print('Other: ' + str(sample2.var()))    
    
    diff = sample1.mean() - sample2.mean()
    
    var1 = sample1.var()
    var2 = sample2.var()
    
    n1, n2 = len(sample1), len(sample2)
    
    pooled_var = (n1*var1 + n2*var2)/ (n1 + n2)
    d = diff/math.sqrt(pooled_var)
    print("Cohen's D: " + str(d))
    return d
