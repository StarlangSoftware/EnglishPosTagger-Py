from Corpus.Sentence import Sentence
from Hmm.Hmm import Hmm
from Hmm.Hmm1 import Hmm1

from PosTagger.PosTaggedCorpus import PosTaggedCorpus
from PosTagger.PosTaggedWord import PosTaggedWord
from PosTagger.PosTagger import PosTagger


class HmmPosTagger(PosTagger):

    __hmm: Hmm

    def train(self, corpus: PosTaggedCorpus):
        """
        Train method for the Hmm pos tagger. The algorithm trains an Hmm from the corpus, where corpus constitutes
        as an observation array.

        PARAMETERS
        ----------
        corpus : Corpus
            Training data for the tagger.
        """
        emittedSymbols = []
        for i in range(corpus.sentenceCount()):
            emittedSymbols.append([])
            for j in range(corpus.getSentence(i).wordCount()):
                word = corpus.getSentence(i).getWord(j)
                if isinstance(word, PosTaggedWord):
                    emittedSymbols[i].append(word.getTag())
        self.__hmm = Hmm1(set(corpus.getTagList()), emittedSymbols, corpus.getAllWordsAsList())

    def posTag(self, sentence: Sentence) -> Sentence:
        """
        Test method for the Hmm pos tagger. For each sentence, the method uses the viterbi algorithm to produce the
        most possible state sequence for the given sentence.

        PARAMETERS
        ----------
        sentence : Sentence
            Sentence to be tagged.

        RETURN
        ------
        Sentence
            Annotated (tagged) sentence.
        """
        result = Sentence()
        tagList = self.__hmm.viterbi(sentence.getWords())
        for i in range(sentence.wordCount()):
            result.addWord(PosTaggedWord(sentence.getWord(i).getName(), tagList[i]))
        return result
