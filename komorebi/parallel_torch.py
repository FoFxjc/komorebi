# -*- coding: utf-8 -*-

import torch
from torch import LongTensor
from torch.autograd import Variable

from komorebi.parallel import ParallelData

class TorchParallelData(ParallelData):
    def __init__(self, *args, **kwargs):
        super(TorchParallelData, self).__init__(*args, **kwargs)
        # PyTorch nonsense with CUDA... -_-|||
        if 'use_cuda' in kwargs:
            self.use_cuda = kwargs['use_cuda']
        else:
            self.use_cuda = torch.cuda.is_available()

    def variable_from_sent(self, sent, vocab):
        """
        Create the PyTorch variable given a sentence

        :param sent: The input sentence to convert to PyTorch Variable
        :type sent: list(str) or str
        :param vocab: self.src_vocab or self.trg_vocab
        :type vocab: gensim.Dictionary
        """
        sent = self.split_tokens(sent) if type(sent) == str else sent
        vsent = self.vectorize_sent(sent, vocab)
        result = Variable(LongTensor(vsent).view(-1, 1))
        return result.cuda() if self.use_cuda else result
