>>> a = arange(12.9, 17.1, 0.8)
>>> a
array([ 12.9,  13.7,  14.5,  15.3,  16.1,  16.9])

>>> a[0] = 99
>>> a
array([ 99. ,  13.7,  14.5,  15.3,  16.1,  16.9])

>>> a[2:5] = 0
>>> a
array([ 99. ,  13.7,   0. ,   0. ,   0. ,  16.9])

>>> a[1:6:2] += 2
>>> a
array([ 99. ,  15.7,   0. ,   2. ,   0. ,  18.9])

