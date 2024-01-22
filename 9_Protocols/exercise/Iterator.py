class NaiveIterator:
    def __init__(self,text):
        self._text = text[:]

    def __iter__(self):
        self._row,self._col = 0,-1
        return self

    def __next__(self):
        self._advance()
        if self._row == len(self._text):
            raise StopIteration
        return self._text[self._row][self._col]

    def _advance(self):
        if self._row < len(self._text):
            self._col += 1
            if self._col == len(self._text[self._row]):
                self._row += 1
                self._col = 0

def gather(buffer):
    result = ''
    for char in buffer:
        result += char
    return result

def test_naive_buffer():
    buffer = NaiveIterator(['ab','c'])
    assert gather(buffer) == 'abc'

test_naive_buffer()