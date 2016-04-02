[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```python
import random

x = [random.random() for _ in range(1000)]
pmf = thinkstats2.Pmf(x)
thinkplot.Pmf(pmf, linewidth = 0.1)
thinkplot.Show()

cdf = thinkstats2.Cdf(x)
thinkplot.Cdf(cdf)
thinkplot.Show()

import scipy.stats

scipy.stats.norm.cdf(0)
```
