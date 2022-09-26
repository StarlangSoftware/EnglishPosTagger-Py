from Corpus.Sentence import Sentence
from DataStructure.CounterHashMap import CounterHashMap

from PosTagger.PosTaggedCorpus import PosTaggedCorpus
from PosTagger.PosTaggedWord import PosTaggedWord
from PosTagger.PosTagger import PosTagger


class NaivePosTagger(PosTagger):

    __max_map: dict

    def train(self, corpus: PosTaggedCorpus):
        """
        Train method for the Naive pos tagger. The algorithm gets all possible tag list. Then counts all
        possible tags (with its counts) for each possible word.

        PARAMETERS
        ----------
        corpus : PosTaggedCorpus
            Training data for the tagger.
        """
        word_map = {}
        for i in range(corpus.sentenceCount()):
            s = corpus.getSentence(i)
            for j in range(s.wordCount()):
                word = corpus.getSentence(i).getWord(j)
                if isinstance(word, PosTaggedWord):
                    if word.getName() in word_map:
                        word_map[word.getName()].put(word.getTag())
                    else:
                        counter_map = CounterHashMap()
                        counter_map.put(word.getTag())
                        word_map[word.getName()] = counter_map
        self.__max_map = {}
        for word in word_map:
            self.__max_map[word] = word_map[word].max()

    def posTag(self, sentence: Sentence) -> Sentence:
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
        result = Sentence()
        for i in range(sentence.wordCount()):
            result.addWord(PosTaggedWord(sentence.getWord(i).getName(), self.__max_map[sentence.getWord(i).getName()]))
        return result
