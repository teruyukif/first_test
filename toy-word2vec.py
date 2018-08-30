# -*- coding: utf-8 -*-

from gensim.models import word2vec
import sys

#学習




#読み込み
model   = word2vec.Word2Vec.load(sys.argv[1])
results = model.most_similar(positive=sys.argv[2], topn=10)
s
