# Tips for accelerating Python code

## Python multiprocessing module

`plot_sdss_spectrum.py` (run with '-h' for usage help) is an example for how to use the multiprocessing module to plot many SDSS spectra in parallel. The results on my laptop (2 real cores, 4 "virtual" Hyperthreaded cores) are shown below. That's about a 2x speedup when using all 4 virtual cores, which is pretty good, considering there's also disk IO involved. There's probably room to make this faster too, though some of it may be limited by matplotlib itself.

```
$ time ./plot_sdss_spectra.py ../../data/spec-*
real    0m22.561s
user    0m21.908s
sys 0m0.543s

$ time ./plot_sdss_spectra.py -mp -p 2 ../../data/spec-*

real    0m15.144s
user    0m28.392s
sys 0m0.782s

$ time ./plot_sdss_spectra.py -mp -p 4 ../../data/spec-*

real    0m12.827s
user    0m39.254s
sys 0m1.077s
```

`real`  = time taken to run, e.g. "wall clock" time

`user + sys`  = CPU time

In the first example (one process), the CPU time is about the same as the clock time. In the second example, the CPU time of 29s exceeds the wall time by 2x, showing that two cores were running. CPU time can exceed wall time when multiple processes are used on a multiple core system.

Run the code with `python -m cProfile -o plotspec.prof plot_sdss_spectrum.py ...` to get a dump of the profiling information. Load and print the profiling data with:

```
import pstats
stats = pstats.Stats('plotspec.prof')
stats.strip_dirs()
stats.sort_stats('cumtime').print_stats(20)
```
See the python profiling page for more on working with pstats data:

https://docs.python.org/2/library/profile.html

### numba

Installed with Anaconda. Simple example:

```
import numpy as np
from numba import vectorize
@vectorize(['float64(float64, float64)'], target='parallel')
def sum(a, b):
   return a + b

N = 10000
xx = np.random.random(N)
yy = np.random.random(N)
sum(xx,yy)
```

