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
