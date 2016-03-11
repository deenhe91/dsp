# Hint:  use Google to find python function

from datetime import datetime

date_format = "%m-%d-%Y"

date_start = datetime.strptime('01-02-2013', date_format)
date_stop = datetime.strptime('07-28-2015', date_format)

delta = date_stop - date_start

print ("a. " + str(delta.days))

date_format = "%m%d%Y"
date_start = datetime.strptime('12312013', date_format)
date_stop = datetime.strptime('05282015', date_format)

delta = date_stop - date_start

print ("b. " + str(delta.days))

date_format = "%d-%b-%Y"
date_start = datetime.strptime('15-Jan-1994', date_format)
date_stop = datetime.strptime('14-Jul-2015', date_format)

delta = date_stop - date_start

print ("c. " + str(delta.days))
