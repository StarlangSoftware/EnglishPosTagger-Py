from abc import abstractmethod

from Corpus.Sentence import Sentence

from PosTagger.PosTaggedCorpus import PosTaggedCorpus


class PosTagger:

    @abstractmethod
    def train(self, corpus: PosTaggedCorpus):
        pass

    @abstractmethod
    def posTag(self, sentence: Sentence) -> Sentence:
        pass
