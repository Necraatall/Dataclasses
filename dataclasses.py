from functools import total_ordering

@total_ordering
class ManualComment:
    def __init__(self, id: int, text: str) -> None:
        self.__id: int = id
        self.__text: str = text


    @property
    def id(self):
        return self.__id

    @property
    def text(self):
        return self.__text

    def __hash__(self):    
        return hash((self.__class__, self.id, self.text))

# sort
    # les than
    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) < (other.id, other.text)
        else:
            return NotImplemented

    # less than equal to
    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) <= (other.id, other.text)
        else:
            return NotImplemented

    # greater than
    def __repr__(self) -> str:
        return "{}(id={}, text={})".format(self.__class__.__name__, self.id, self.text)

    # equal
    def __eq__(self, other) -> bool:
        if other.__class__ is self.__class__:
            return (self.id, self.text) == (other.id, other.text)
        else:
            return NotImplemented

    # greater or equal to method
    def __ne__(self, other) -> bool:
        if other.__class__ is self.__class__:
            return (self.id, self.text) >= (other.id, other.text)
        else:
            return NotImplemented


