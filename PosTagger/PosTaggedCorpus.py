from collections import KeysView

from Corpus.Corpus import Corpus
from Corpus.Sentence import Sentence
from DataStructure.CounterHashMap import CounterHashMap

from PosTagger.PosTaggedWord import PosTaggedWord
import re


class PosTaggedCorpus(Corpus):

    __tagList: CounterHashMap

    """
    A constructor of PosTaggedCorpus which initializes the sentences of the corpus, the word list of
    the corpus, and all possible tags.

    PARAMETERS
    ----------
    fileName : str
        Name of the corpus file.
    """
    def __init__(self, fileName:str = None):
        self.sentences = []
        self.wordList = CounterHashMap()
        self.__tagList = CounterHashMap()
        newSentence = Sentence()
        if fileName is not None:
            inputFile = open(fileName, "r", encoding="utf8")
            lines = inputFile.readlines()
            for line in lines:
                words = re.split("[\t\n ]", line)
                for word in words:
                    if len(word) > 0 and "/" in word:
                        name = word[:word.rindex("/")]
                        tag = word[word.rindex("/") + 1:]
                        if "+" in tag:
                            shortTag = tag[:tag.index("+")]
                        elif "-" in tag:
                            shortTag = tag[:tag.index("-")]
                        else:
                            shortTag = tag
                        self.__tagList.put(shortTag)
                        newSentence.addWord(PosTaggedWord(name, shortTag))
                        if tag == '.':
                            self.addSentence(newSentence)
                            newSentence = Sentence()
            if newSentence.wordCount() > 0:
                self.addSentence(newSentence)

    """
    getTagList returns all possible tags as a set.

    RETURNS
    -------
    set
        Set of all possible tags.
    """
    def getTagList(self) -> KeysView:
        return self.__tagList.keys()
