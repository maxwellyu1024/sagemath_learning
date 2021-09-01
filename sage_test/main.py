#!/usr/bin/env sage

import time
from sage.all import *

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

if len(sys.argv) != 2:
    print("Usage: %s <n>" % sys.argv[0])
    print("Outputs the prime factorization of n.")
    sys.exit(1)
else:
    print(factor(sage_eval(sys.argv[1])))

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
