import string

from insert_delete import InsertDeleteApp

class Action:
    def __init__(self,app):
        self._app = app

    def do(self):
        raise NotImplementedError(f"{self.__class__.__name__}: do")

    def undo(self):
        raise NotImplementedError(f"{self.__class__.__name__}: undo")

    def save(self):
        return True

class Insert(Action):
    def __init__(self,app,pos,char):
        super().__init__(app)
        self._pos = pos
        self._char = char

    def do(self):
        self._app._buffer.insert(self._pos,self._char)

    def undo(self):
        self._app._buffer.delete(self._pos)

    def __str__(self):
        return f"Insert({self._pos},'{self._char}')"

class Delete(Action):
    def __init__(self,app,pos):
        super().__init__(app)
        self._pos = pos
        self._char = self._app._buffer.char(pos)

    def do(self):
        self._app._buffer.delete(self._pos)

    def undo(self):
        self._app._buffer.insert(self._pos,self._char)

    def __str__(self):
        return f"Delete({self._pos},'{self._char}')"



class Move(Action):
    def __init__(self,app,direction):
        