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

class Playlist(list):
    def __init__(self, nome, programas = []):
        self.nome = nome
        super().__init__(programas)

vingadores = Filme('Vingadores - Guerra Infinta', 2018, 160)
atlanta = Serie('Atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
[tmep.dar_like() for i in range(4)]
[demolidor.dar_like() for i in range(2)]
[atlanta.dar_like() for i in range(3)]

playlist_fim_de_semana = Playlist('fim de semana')
# Note o reúso do método 'append'.
playlist_fim_de_semana.append(vingadores)
playlist_fim_de_semana.append(atlanta)
playlist_fim_de_semana.append(demolidor)
playlist_fim_de_semana.append(tmep)

# Note o reúso do comportamento de um list ao invocarmos o método 'len()'.
print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}.\n')

# Mais um reúso: o comportamento da playlist como iterable.
for programa in playlist_fim_de_semana:
    print(programa)

# Outro reúso: a função 'in' testa existência de uma instância na lista.
print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}.')
