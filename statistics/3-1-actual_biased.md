[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> import chap01soln
resp = chap01soln.ReadFemResp()

num_pmf = thinkstats2.Pmf(resp.numkdhh)
thinkplot.Pmf(num_pmf, label = 'actual')

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

biased_num = BiasPmf(num_pmf, label = ' ')

thinkplot.Pmf(biased_num, label='observed')

thinkplot.PrePlot(2)
thinkplot.Pmfs([num_pmf, biased_num])
thinkplot.Show(xlabel = 'no. of children', ylabel = 'PMF')

