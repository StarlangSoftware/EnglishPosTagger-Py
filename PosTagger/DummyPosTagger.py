from Corpus.Sentence import Sentence

from PosTagger.PosTaggedCorpus import PosTaggedCorpus
from PosTagger.PosTaggedWord import PosTaggedWord
from PosTagger.PosTagger import PosTagger
import random


class DummyPosTagger(PosTagger):

    __tagList: list

    def train(self, corpus: PosTaggedCorpus):
        corpusTagList = corpus.getTagList()
        self.__tagList = list(corpusTagList)

    def posTag(self, sentence: Sentence) -> Sentence:
        """
        Test method for the Dummy pos tagger. For each word, the method chooses randomly a tag from all possible
        tag list.

        PARAMETERS
        ----------
        sentence : Sentence
            Sentence to be tagged.

        RETURNS
        -------
        Sentence
            Annotated (tagged) sentence.
        """
        result = Sentence()
        for i in range(sentence.wordCount()):
            index = random.randint(0, len(self.__tagList) - 1)
            result.addWord(PosTaggedWord(sentence.getWord(i).getName(), self.__tagList[index]))
        return result
