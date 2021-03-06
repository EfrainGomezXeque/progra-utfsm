Creación de arreglos bidimensionales
====================================

La función ``arange`` retorna un arreglo
con números en el rango indicado::

    >>> from numpy import arange
    >>> a = arange(12)
    >>> a
    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

A partir del arreglo ``a`` definido arriba,
indique cómo obtener los siguientes arreglos
de la manera más simple que pueda::

    >>> # ???
    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])
    >>> # ???
    array([[  0,   1,   4,   9],
           [ 16,  25,  36,  49],
           [ 64,  81, 100, 121]])
    >>> # ???
    array([[ 0,  4,  8],
           [ 1,  5,  9],
           [ 2,  6, 10],
           [ 3,  7, 11]])
    >>> # ???
    array([[ 0,  1,  2],
           [ 4,  5,  6],
           [ 8,  9, 10]])
    >>> # ???
    array([[ 11.5,  10.5,   9.5],
           [  8.5,   7.5,   6.5],
           [  5.5,   4.5,   3.5],
           [  2.5,   1.5,   0.5]])
    >>> # ???
    array([[100, 201, 302, 403],
           [104, 205, 306, 407],
           [108, 209, 310, 411]])
    >>> # ???
    array([[100, 101, 102, 103],
           [204, 205, 206, 207],
           [308, 309, 310, 311]])
