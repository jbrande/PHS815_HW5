# PHSX815 Spring 2021 Week 5

## Rejection Sampling

The python scripts require the following libraries: `numpy` and `matplotlib`

### Usage

All of the executables can be called from the
command line with the `-h` or `--help` flag, which will print the options

The python scripts can be run with the following options
- `python python/RejectSample.py -Nsample [# samples]`
- `python python/SampleShape.py -Nsample [# samples]`

RejectSample.py will use rejection sampling to estimate the integral of sin(pi\*x) between 0 and 1. The results are plotted in calcInt.jpg and plotInt.jpg.

SampleShape.py will use rejection sampling to estimate the area intersected by two circles (x-0.5)^2 + y^2 = 1 and (x+0.5)^2 + y^2 = 1. The results are plotted in calcCirc.jpg and plotCirc.jpg.