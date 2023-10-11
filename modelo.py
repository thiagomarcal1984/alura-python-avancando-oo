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
    
class Filme(Programa):
    def __init__(self, nome, ano, duracao) -> None:
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas) -> None:
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme('Vingadores - Guerra Infinta', 2018, 160)
vingadores.dar_like()
print(f'{vingadores.nome} - {vingadores.duracao} - {vingadores.likes}')


atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.nome = 'atlanta' # Agora esta atribuição sempre será titulada, pois está encapsulada.
print(f'{atlanta.nome} - {atlanta.temporadas} - {atlanta.likes}')

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(f'{programa.nome} - {detalhes} - {programa.likes}')
