import numpy as np
for x in [1,10,1000]:
    a = np.exp(1/np.sin(x) + 1)
    b = 5/4 + 1/x**1.5
    y = np.log(a/b)/np.log(1+x**2)
    print(y)


#ybase = np.log(1+x**2)
#ysol = np.log