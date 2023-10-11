class Programa:
    def __init__(self, nome, ano) -> None:
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo__nome):
        self.__nome = novo__nome.title()

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} Likes'

    
class Filme(Programa):
    def __init__(self, nome, ano, duracao) -> None:
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas) -> None:
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes'

vingadores = Filme('Vingadores - Guerra Infinta', 2018, 160)
vingadores.dar_like()

atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)
