from abc import abstractmethod


class PosTagger:

    @abstractmethod
    def train(self, corpus: PosTaggedCorpus):
        pass

    @abstractmethod
    def posTag(self, sentence: Sentence):
        pass