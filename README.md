
Install
====

```
pip3 install -U komorebi
```

Usage
====


```python
$ cut -f1 data/kopitiam/kopitiam.tsv | tail -n +2 > kopitiam.sg
$ cut -f2 data/kopitiam/kopitiam.tsv | tail -n +2 > kopitiam.en

>>> from komorebi import TorchParallelData as ParallelData

>>> sgfile = 'data/kopitiam/kopitiam.sg'
>>> enfile = 'data/kopitiam/kopitiam.en'

>>> x = ParallelData(sgfile, enfile)
Building source vocab and counter... populate_dictionary took 00:00:00
Building target vocab and counter... populate_dictionary took 00:00:00
Filtering least frequent words in vocab.

>>> next(x)
(Variable containing:
 0
 3
 4
 1
[torch.LongTensor of size 4x1]
, Variable containing:
 0
 3
 4
 6
 5
 1
[torch.LongTensor of size 6x1]
)

>>> next(x)
(Variable containing:
 0
 3
 1
[torch.LongTensor of size 3x1]
, Variable containing:
    0
    3
    4
    6
    7
    8
    1
[torch.LongTensor of size 7x1]
)

>>> next(x)
(Variable containing:
 0
 3
 5
 1
[torch.LongTensor of size 4x1]
, Variable containing:
    0
    3
    4
    6
    9
    8
    1
[torch.LongTensor of size 7x1]
)

>>> x.reset()

>>> x.save('kopital-data')
Saving ParallelData to kopital-data save took 00:00:00

>>> y = ParallelData(loadfrom='kopital-data')
Loading ParallelData from kopital-data/ParallelData.json load took 00:00:00


>>> next(y)
(Variable containing:
 0
 3
 4
 1
[torch.LongTensor of size 4x1]
, Variable containing:
 0
 3
 4
 6
 5
 1
[torch.LongTensor of size 6x1]
)
>>> next(y)
(Variable containing:
 0
 3
 1
[torch.LongTensor of size 3x1]
, Variable containing:
    0
    3
    4
    6
    7
    8
    1
[torch.LongTensor of size 7x1]
)
>>> y.reset()

>>> next(y)
(Variable containing:
 0
 3
 4
 1
[torch.LongTensor of size 4x1]
, Variable containing:
 0
 3
 4
 6
 5
 1
[torch.LongTensor of size 6x1]
)
```

**Shuffling the data**

```python
>>> from komorebi import TorchParallelData as ParallelData
>>> sgfile = 'data/kopitiam/kopitiam.sg'
>>> enfile = 'data/kopitiam/kopitiam.en'
>>> x = ParallelData(sgfile, enfile)
Building source vocab and counter... populate_dictionary took 00:00:00
Building target vocab and counter... populate_dictionary took 00:00:00
Filtering least frequent words in vocab.

>>>
>>> for sg, en in x.shuffle():
...     print(sg)
...     print(en)
...     break
...
Variable containing:
 0
 3
 5
 1
[torch.LongTensor of size 4x1]

Variable containing:
    0
    3
    4
    6
    9
    8
    1
[torch.LongTensor of size 7x1]
```
