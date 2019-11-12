from Corpus.Sentence import Sentence
from DataStructure.CounterHashMap import CounterHashMap

from PosTagger.PosTaggedCorpus import PosTaggedCorpus
from PosTagger.PosTaggedWord import PosTaggedWord
from PosTagger.PosTagger import PosTagger


class NaivePosTagger(PosTagger):

    __maxMap: dict

    """
    Train method for the Naive pos tagger. The algorithm gets all possible tag list. Then counts all
    possible tags (with its counts) for each possible word.

    PARAMETERS
    ----------
    corpus : PosTaggedCorpus
        Traning data for the tagger.
    """
    def train(self, corpus: PosTaggedCorpus):
        map = {}
        for i in range(corpus.sentenceCount()):
            s = corpus.getSentence(i)
            for j in range(s.wordCount()):
                word = corpus.getSentence(i).getWord(j)
                if word in map:
                    map[word.getName()].put(word.getTag())
                else:
                    counterMap = CounterHashMap()
                    counterMap.put(word.getTag())
                    map[word.getName()] = counterMap
        self.__maxMap = {}
        for word in map:
            self.__maxMap[word] = map[word].max()

    """
    Test method for the Naive pos tagger. For each word, the method chooses the maximum a posterior tag from all
    possible tag list for that word.

    PARAMETERS
    ----------
    sentence : Sentence
        Sentence to be tagged.
        
    RETURNS
    -------
    Sentence
        Annotated (tagged) sentence.
    """
    def posTag(self, sentence: Sentence) -> Sentence:
        result = Sentence()
        for i in range(sentence.wordCount()):
            result.addWord(PosTaggedWord(sentence.getWord(i).getName(), self.__maxMap[sentence.getWord(i).getName()]))
        return result
