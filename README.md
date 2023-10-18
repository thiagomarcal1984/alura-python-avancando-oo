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

# Para saber mais: Atributos de classe

Quando criamos atributos no inicializador, estamos definindo quais serão as características do objeto sendo definido. Mas esta não é a única forma de adicionar características ao objeto ou mesmo à classe.

O aspecto dinâmico da linguagem permite que seja possível adicionar atributos até sem precisar do `__init__`. Veja abaixo:
```python
class Pessoa:
    pass

pessoa = Pessoa()
pessoa.nome = 'Jade'
print(pessoa.nome)
```
Se você tentar executar este código, verá que funciona perfeitamente.

Optamos em usar o inicializador, primeiro para facilitar a criação de novos objetos e segundo para diminuir a confusão em saber o que a classe precisa para criar um objeto aceitável. Sem o init, não dá para saber facilmente quais atributos a classe possui.

Normalmente usamos o init para definir os atributos, mas o que fazer se precisarmos definir um valor padrão para todos os objetos? Ou até criar um atributo que será compartilhado para todas as instâncias?

Para isto, vai ser necessário criar um atributo ligado à classe, ao invés de ligado à instância (`self`). Por exemplo:

```python
class Pessoa:
    tamanho_cpf = 11

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def valida_cpf(self):
        return True if len(self.cpf) == __class__.tamanho_cpf else False

pe = Pessoa('00000000001', 'Ruby')
print(pe.valida_cpf())

pe = Pessoa('0000000000', 'Cristal')
print(pe.valida_cpf())
```
Veja como o valor de `tamanho_cpf` é usado por todas as instâncias.

Esse é um atributo de classe. É possível alterar o valor deste atributo, mudando seu estado e não é necessário criar uma instância para acessá-lo.

No trecho de código acima, precisamos usar o `__class__` para definir que queremos o atributo de classe. Dentro do nosso método de instância precisamos fazer desta forma.

Se não fizermos deste jeito, podemos ter problemas, como no código abaixo. Faça um teste:

```python
class Pessoa:
    tamanho_cpf = 11

p = Pessoa()

print(p.tamanho_cpf)

p.tamanho_cpf = 12

print(p.tamanho_cpf)

print(Pessoa.tamanho_cpf)
```
O que acontece é que, caso não exista o atributo `tamanho_cpf` na instância, o Python busca o atributo na classe. Em seguida, adicionamos um atributo `tamanho_cpf` na instância e quando dizemos que o valor é 12, o atributo da classe não é alterado, já que são atributos diferentes, um da classe e outro só da instância.

Código da arquivo `pessoa.py`:
```python
class Pessoa:
    tamanho_cpf = 11

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def valida_cpf(self):
        return True if len(self.cpf) == __class__.tamanho_cpf else False

pe = Pessoa('00000000001', 'Ruby')
print(pe.valida_cpf())

pe = Pessoa('0000000000', 'Cristal')
print(pe.valida_cpf())

# Redefinição da classe Pessoa:
class Pessoa:
    tamanho_cpf = 11

p = Pessoa()

print(f'Tamanho CPF na instância: {p.tamanho_cpf}')
print(f'Mudando o tamanho do CPF no objeto para 12...')

p.tamanho_cpf = 12

print(f'Tamanho CPF na instância: {p.tamanho_cpf}')

print(f'Tamanho CPF na classe: {Pessoa.tamanho_cpf}')
print(f'Tamanho CPF na classe: {p.__class__.tamanho_cpf}')
```
# Removendo duplicação
Em Python, a herança é declarada sufixando entre parenteses o nome da classe extendida:
```python
classe Filha(Mae):
    def __init__(self, atributo_especifico)
    super().__init__(atributo_geral)
    self.atributo_especifico = atributo_especifico
``` 
## Name mangling
No Python, os atributos privados não são herdados. Isso acontece por causa do `name mangling` (ou `name decoration`), uma forma de mudar o nome de atributos privados para o padrão `_Classe__atributo` no Python.

Exemplo da classe `Filme`:
```python
class Filme(Programa):
    def __init__(self, nome, ano, duracao) -> None:
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0
        self.duracao = duracao

# Resto do código

vingadores = Filme('Vingadores - Guerra Infinta', 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f'- Duração: {vingadores.duracao} - Likes: {vingadores.likes}')
```
A saída desse programa será: 
```
PS D:\alura\python-avancando-oo> python .\modelo.py
Traceback (most recent call last):
  File "D:\alura\python-avancando-oo\modelo.py", line 37, in <module>        
    vingadores.dar_like()
  File "D:\alura\python-avancando-oo\modelo.py", line 12, in dar_like        
    self.__likes += 1
    ^^^^^^^^^^^^
AttributeError: 'Filme' object has no attribute '_Programa__likes'
```

Uma maneira de contornar o `name mangling` é mudar os nomes das propriedades privadas, prefixando com um único underscore ao invés de dois (note os atributos `_nome` e `_likes` no código do arquivo `modelo.py`):
```python
class Programa:
    def __init__(self, nome, ano) -> None:
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
class Filme(Programa):
    def __init__(self, nome, ano, duracao) -> None:
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, nome, ano, temporadas) -> None:
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
        self.temporadas = temporadas

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
> O código volta a funcionar, mas há um problema: a duplicação das variáveis `_nome` e `_likes` nas classes mãe e filha. Como resolver?

# Reutilizando ainda mais
Para construir o objeto a partir do construtor da classe mãe, use a função `super().__init__(parametros_da_classe_mae)`. A função `super()` referencia a classe mãe, enquanto a função `__init__(parms)` preenche a instância com o construtor da classe mãe.

Código do arquivo `modelo.py`:
```python
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
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f'- Duração: {vingadores.duracao} - Likes: {vingadores.likes}')


atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
atlanta.nome = 'atlanta' # Agora esta atribuição sempre será titulada, pois está encapsulada.
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
      f'- Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')
```

# Explicando a herança
Benefícios da herança:
1. reúso de atributos e métodos (não é necessário redeclarar dados e comportamento nas classes filhas);
2. extensão por meio da sobre-escrita de métodos (no exemplo, o método construtor das classes filha usa o construtor da classe mãe e adiciona atribuições inexistentes na classe mãe);
3. atributos e métodos específicos se limitam à classse específica (a classe mãe e as classes irmãs não precisam conhecer o código da classe filha atual).

# Para saber mais: Métodos estáticos e de classe

Da mesma forma que temos alguns atributos diretamente da classe, e que são acessíveis sem necessidade de criar uma instância, conseguimos também criar métodos ligados à classe.

Há duas formas de criar estes métodos:

## Métodos de classe
São métodos declarados com `@classmethod`. Quando criamos um método de classe, temos acesso aos atributos da classe. Da mesma forma com os atributos de classe, podemos acessar estes métodos de dentro dos métodos de instância, a partir de `__class__`, se desejarmos:

```python
class Funcionario:
    prefixo = 'Instrutor'

    @classmethod
    def info(cls):
        return f'Esse é um {cls.prefixo}'
```

Perceba que, ao invés de `self`, passamos `cls` para o método, já que neste caso sempre recebemos uma instância da classe como primeiro argumento. O nome `cls` é uma convenção, assim como `self`.

## Métodos estáticos
A outra forma de criar métodos ligados à classe é com a declaração `@staticmethod`. Veja abaixo:

```python
class FolhaDePagamento:
    @staticmethod
    def log():
        return f'Isso é um log qualquer'
```

Note que, no caso acima, não precisamos passar nenhum primeiro argumento fixo para o método estático. Nesse caso, não é possível acessar as informações da classe, porém o método estático é acessível a partir da classe e também da instância.

## Cuidados a tomar...
Sempre que você usar métodos estáticos em classes que contém herança, observe se não está tentando acessar alguma informação da classe a partir do método estático, pois isso pode dar algumas dores de cabeça pra entender o motivo dos problemas.

Alguns pythonistas não aconselham o uso do `@staticmethod`, já que poderia ser substituído por uma simples função no corpo do módulo. Outros mais puristas entendem que os métodos estáticos fazem sentido, sim, e que devem ser vistos como responsabilidade das classes.

# Polimorfismo
Objetos que compartilham a mesma classe mãe apresentam formas diferentes de se comportar. Por isso que a herança possibilita o polimorfismo.

As classes `Filme` e `Serie` compartilham os getters para nome e likes. Então esses getters podem ser chamados sem quaisquer testes.

Mas duração (atributo de Filme) e temporadas (atributo de Série) são detalhes específicos de cada uma dessas classes. Para exibi-los, seria necessário testá-los com um `if`.

O Python dispõe de um operador ternário com estrutura `<resultado_se_verdadeiro> if <boolean> else <resultado_se_falso>`. No exemplo, usaremos uma função que testa a existência de um atributo (a função `hasattr(objeto, 'nome_do_atributo')`).

Código do arquivo `modelo.py`:
```python
# Resto do código
filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(f'{programa.nome} - {detalhes} - {programa.likes}')
```

# Reduzindo ifs
Uma forma de reduzir os ifs é declarar um método na superclasse e redefinir (sobreescrever) esse método nas classes filhas. Neste caso, vamos implementar o método `imprime(self)`:

```python
class Programa:
    def __init__(self, nome, ano) -> None:
        # Resto do código

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.likes} Likes')

    
class Filme(Programa):
    def __init__(self, nome, ano, duracao) -> None:
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas) -> None:
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes')

vingadores = Filme('Vingadores - Guerra Infinta', 2018, 160)
vingadores.dar_like()

atlanta = Serie('Atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    programa.imprime()
```

Resultado do programa:
```
PS D:\alura\python-avancando-oo> python .\modelo.py
Vingadores - Guerra Infinta - 2018 - 160 min - 1 Likes
Atlanta - 2018 - 2 temporadas - 2 Likes
```
> Note que não é mais necessário inserir o `if` dentro do `for`: o método `imprime(self)`, devido ao seu polimorfismo, exibe informações diferentes a depender do tipo de objeto que está sendo impresso.

# Representação textual de objetos
Há um método especial (dunder method) chamado `__str__(self)` que serve para representar o objeto como string. O método `imprime(self)` será substituído por este dunder method.

```python
class Programa:
    # Resto do código
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} Likes'

    
class Filme(Programa):
    # Resto do código
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes'

class Serie(Programa):
    # Resto do código
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes'

# Resto do código 

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)
```
> O dunder method `__repr__(self)` é semelhante ao `__str__(self)`. A diferença dos dois é semântica: `repr()` é uma representação imprimível do objeto que o torne inconfundível, enquanto `str()` é uma representação legível para humanos.

# Para saber mais: Outra forma de representação

Nós vimos como usar `__str__` para representar um objeto como string de forma legível.

Falamos sobre uma outra forma de representação, ela pode ajudar bastante se precisarmos encontrar um erro, ou debugar o código.

Assim como o `__str__`, existe outro método especial chamado `__repr__`, que é usado para mostrar uma representação que ajude no debug ou log de um código.

Por exemplo, se você quiser entender como funciona seu objeto, ou se está válido, e imprimir o seu valor string, qual resultado abaixo facilita sua vida?

```python
> Filme(nome='vingadores', ano=2018, duracao=160)
```
Ou:

```python
> "Filme: Vingadores de 2018 - 160 min"
```

A primeira deixa bem claro como funciona o objeto. Normalmente, a segunda forma ilustra o que um usuário final ficaria satisfeito em ver.

A ideia da primeira versão é remover ambiguidade e permite, por exemplo, recriar o objeto, já que está mostrando todas as informações.

Outro exemplo, se chamarmos o `repr` de um objeto do tipo `list`, podemos ter uma ideia do que é esperado quando criarmos o nosso próprio com `__repr__`:

```python
lista = [1, 2, 4, 5]

print(repr(lista))
```

Se pegarmos o resultado do print, conseguimos recriar o objeto lista.

# Criando a playlist
Código do arquivo `modelo.py`:
```python
# Resto do código

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def tamanho(self):
        return len(self.programas)

vingadores = Filme('Vingadores - Guerra Infinta', 2018, 160)
atlanta = Serie('Atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
[tmep.dar_like() for i in range(4)]
[demolidor.dar_like() for i in range(2)]
[atlanta.dar_like() for i in range(3)]

filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana.programas:
    # Note que para iterarmos na playlist,
    # precisaríamos conhecer o atributo 'programas'.
    print(programa)
```

Para aumentar o encapsulamento da classe `Playlist`, seria interessante não permitir o acesso ao atributo interno `programas`. A classe `Playlist` também poderia estender algum objeto iterável.

# Reaproveitando um list
Existe o tipo `list`, que na verdade é uma classe que implementa `iterable`!

Assim, podemos estender a classe `list` para herdar alguns comportamentos

```python
class Playlist(list):
    def __init__(self, nome, programas = []):
        self.nome = nome
        super().__init__(programas)

#Resto do código
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
```

# Fugindo da complexidade
Uma desvantagem da herança: a classe estendida pode ter muitos métodos e atributos desconhecidos pelo desenvolvedor. Há o risco de esses métodos e atributos serem sobre-escritos, e assim a classe filha deixa de funcionar corretamente.

Modificação do código do arquivo `modelo.py`, após remover a herança e inserir métodos para a lista e o tamanho da lista:
```python
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.__programas = programas

    @property
    def listagem(self):
        return self.__programas

    @property
    def tamanho(self):
        return len(self.__programas)

# Resto do código
filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {playlist_fim_de_semana.tamanho}.\n')

# Mais um reúso: o comportamento da playlist como iterable.
for programa in playlist_fim_de_semana.listagem:
    print(programa)
```
# Se anda como um pato...
O comportamento iterável de um objeto pode ser (re)definido por meio do dunder method `__getitem__(self, item)`. Isso permite que o objeto que implementa esse dunder method use o operador `in` e a iteração com o laço `for`.

```python
class Playlist:
    # Resto do código
    def __getitem__(self, item):
        return self.__programas[item]

# Resto do código

for programa in playlist_fim_de_semana:
    print(programa)

print(vingadores in playlist_fim_de_semana[1:]) # False
print(playlist_fim_de_semana[0]) # Mostra somente o filme Vingadores.
```

> Não importa se o objeto dentro do for é ou não uma lista. Se ela faz tudo que uma lista faz (é percorrível com for, pode ter seus itens acessados isoladamente, pode ser fatiada etc), ela é uma lista (mesmo que não herde de lista).
> 
> Duck typing: Se anda como pato, voa como pato e nada como um pato, é um pato.

# Modelo de dados Python
Para adicionar o comportamento de sizeable (para usar a playlist como parâmetro da função `len`), implementamos o magic/dunder method `__len__(self)`:
```python
class Playlist:
    # Resto do código
    def __len__(self):
        return len(self.__programas)

# Resto do código 
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}.\n')
```
## Python Data Model
Há alguns magic/dunder methods que compõem os objetos do Python. Eis os mais comuns:
1. Inicialização: `__init__`;
2. Representação: `__str__`, `__repr__`;
3. Container/sequência: `__contains__`, `__iter__`, `__len__`, `__getitem__`;
4. Numéricos: `__add__`, `__sub__`, `__mul__`, `__mod__`.

# Classes abstratas ou ABCs
Existe no Python o pacote `abc` que contém o objeto `ABC`. Sim, existe esse pacote e essa classe, e eles representam uma `Abstract Base Class`.

Outros pacotes também tem os pacotes `abc`, como `collections` ou `numbers`.

Exemplo de ABC de `collections` (arquivo `playlist.py`):

```python
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
```
Exemplo de ABC de `numbers` (arquivo `numero_complexo.py`):
```python
from numbers import Complex
class Numero(Complex):
    pass

# A criação do objeto abaixo vai apresentar o seguinte erro:
# TypeError: Can't instantiate abstract class Numero with abstract 
# methods __abs__, __add__, __complex__, __eq__, __mul__, __neg__, __pos__, 
# __pow__, __radd__, __rmul__, __rpow__, __rtruediv__, __truediv__, conjugate, imag, real
num = Numero()
```
# Para saber mais: Criando ABC

Verificamos que é possível usar classes abstratas do sistema, e conseguimos alguns benefícios de bandeja, por exemplo:
- Tenho um erro que me diz, em tempo de instanciação, se eu esqueci de implementar algum método da superclasse;
- E também sou impedido de instanciar um objeto do tipo da superclasse, pra não ter problema com os métodos abstratos;
- Ainda posso aproveitar código dos meus métodos abstratos (que podem ter implementação na classe mãe).

Se você ficou com curiosidade sobre como criar uma classe abstrata, vamos pensar no seguinte caso: imagine que não queremos permitir que ninguém instancie um objeto da classe `Programa`, e queremos garantir que todo mundo implemente o `__str__` nas suas subclasses. Parece uma boa ideia.

Para fazer isso, o nosso código ficaria assim:

```python
from abc import ABCMeta, abstractmethod 
class Programa(metaclass = ABCMeta): 
    @abstractmethod 
    def __str__(self): 
        pass
```
> Note a herança de `metaclass = ABCMeta` e a anotação `@abstractmethod` no método que queremos forçar a implementação.

Apenas com isso, podemos garantir que o `__str__` será implementado nas nossas subclasses, se não for implementado em alguma, será avisado em tempo de instanciação (não vai conseguir criar instâncias).
