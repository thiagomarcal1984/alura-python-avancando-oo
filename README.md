# Relembrando classes e objetos
Modelagem de um Filme:
- nome
- ano
- duração

Modelagem de uma Série:
- nome
- ano
- temporadas

Nas próximas aulas vamos adicionar um atributo chamado `likes`, além de acrescentarmos um comportamento de colocar iniciais maiúsculas no nome do filme ou da série.

Código inicial do arquivo `modelo.py`:

```python
class Filme:
    def __init__(self, nome, ano, duracao) -> None:
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:
    def __init__(self, nome, ano, temporadas) -> None:
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

vingadores = Filme('Vingadores - Guerra Infinta', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f'- Duração: {vingadores.duracao}')

atlanta = Serie('Atlanta', 2018, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
      f'- Temporadas: {atlanta.temporadas}')
```
> Note que f-strings podem ser quebradas, desde que cada quebra seja seguida de outra f-string.

# Adicionando atributos e métodos
Implementação do método `dar_like()` e colocação de iniciais maiúsculas no nome dos vídeos usando a função `string.title()`:

```python
class Filme:
    def __init__(self, nome, ano, duracao) -> None:
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes += 1

class Serie:
    def __init__(self, nome, ano, temporadas) -> None:
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.likes += 1

vingadores = Filme('Vingadores - Guerra Infinta', 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f'- Duração: {vingadores.duracao} - Likes: {vingadores.likes}')


atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.nome = 'atlanta' # Falha no encapsulamento.
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
      f'- Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')
```
> Note que há um problema no encapsulamento das propriedades dos objetos: a intenção é que o nome permaneça com iniciais maiúsculas.

# Encapsulando comportamento
Os atributos `nome` e  `likes` terão seus getters encapsulados usando o decorator `@property`, e os seus setters encapsulados usando o decorator `@<propriedade>.setter`. Note que é necessário tornar esses atributos privados, prefixando-os com double underscore. O atributo `likes` não vai ter um setter, e o setter do atributo `nome` sempre colocar as strings com iniciais maiúsculas.

Código do arquivo `modelo.py`:
```python
class Filme:
    def __init__(self, nome, ano, duracao) -> None:
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
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
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
    
class Serie:
    def __init__(self, nome, ano, temporadas) -> None:
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
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
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
    
vingadores = Filme('Vingadores - Guerra Infinta', 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f'- Duração: {vingadores.duracao} - Likes: {vingadores.likes}')


atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.nome = 'atlanta' # Agora esta atribuição sempre será titulada, pois está encapsulada.
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
      f'- Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')
```
