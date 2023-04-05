"""
Write a Python program to count repeated characters in a string. Go to the editor
Sample string: "themorganhouselmoney"
Expected output :
o 3
h 2
e 3
m 2
n 2
"""

import collections
str = 'themorganhouselmoney'
d = collections.defaultdict(int)
for c in str:
    d[c] = d[c] + 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))