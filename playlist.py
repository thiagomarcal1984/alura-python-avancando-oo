from abc import ABC
from collections.abc import MutableSequence

class Playlist(MutableSequence):
    pass

# A criação do objeto abaixo vai apresentar o seguinte erro:
# TypeError: Can't instantiate abstract class Playlist with abstract 
# methods __delitem__, __getitem__, __len__, __setitem__, insert
# filmes = Playlist()

class Playlist(MutableSequence):
    def __getitem__(self, item):
        super().__getitem__(item) # Força reúso do método da superclasse.

    def __setitem__(self, item):
        super().__setitem__(item) # Força reúso do método da superclasse.

    def __len__(self):
        super().__setitem__() # Força reúso do método da superclasse.

# A criação do objeto abaixo vai apresentar o seguinte erro:
# TypeError: Can't instantiate abstract class Playlist with abstract 
# methods __delitem__, insert

filmes = Playlist()
# Note que o erro não fala mais dos dunder methods __getitem__, __setitem__ e __len__.
