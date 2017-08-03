"""
1. Multi Processing Snippets
"""

"""
Example 1
Basic
"""

from multiprocessing import Pool


def f(x):
    return x * x


number_of_processes = 3
data = [1, 2, 3]
p = Pool(number_of_processes)
print(p.map(f, data))

"""

"""


