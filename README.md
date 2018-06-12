
Install
====

```
pip3 install -U komorebi
```

Usage
====


```
from komorebi import ParallelData
sgfile = 'data/kopitiam/kopitiam.sg'
enfile = 'data/kopitiam/kopitiam.en'
x = ParallelData(sgfile, enfile)

next(x)

next(x)

next(x)

x.reset()


x.save('kopital-data')

y = ParallelData(loadfrom='kopital-data')

next(y)
next(y)
y.reset()

```
