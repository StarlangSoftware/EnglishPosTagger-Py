from Dictionary.Word import Word


class PosTaggedWord(Word):

    __tag: str

    """
    A constructor of PosTaggedWord which takes name and tag as input and sets the corresponding attributes

    PARAMETERS
    ----------
    name : str
        Name of the word
    tag : str
        Tag of the word
    """
    def __init__(self, name: str, tag: str):
        super().__init__(name)
        self.__tag = tag

    """
    Accessor method for tag attribute.

    RETURNS
    -------
    str
        Tag of the word.
    """
    def getTag(self) -> str:
        return self.__tag
