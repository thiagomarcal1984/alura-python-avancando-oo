# Herança
## Criando a classe ItemCardapio
Vamos criar dentro do diretório `modelos/cardapio` uma superclasse chamada `ItemCardapio` e as suas subclasses `Prato` e `Bebida`.

A implementação será a seguinte: 

```python
# modelos/cardapio/item_cardapio.py
class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
```
```python
# modelos/cardapio/prato.py
class Prato:
    def __init__(self, nome, preco, descricao):
        pass
        
# modelos/cardapio/bebida.py
class Bebida:
    def __init__(self, nome, preco, tamanho):
        pass
```
Por ora, a relação de herança não foi estabelecida. Na próxima aula isso será realizado.

## Herança
Herança de classe é muito fácil com Python: basta seguir a seguinte sintaxe:
```python
import SuperClasse

class ClasseFilha(SuperClasse):
    pass
```

Vamos fazer as classes `Prato` e `Bebida` herdar da classe `ItemCardapio`:
```Python
# modelos/cardapio/bebida.py
from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

# modelos/cardapio/prato.py
from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
```
> A função `super()` retorna a classe mãe. Dentro do construtor da classe filha é necessário usar o construtor da classe mãe, usando `super().__init__(parametros)` (note que não foi necessário incluir o parâmetro `self` no construtor da superclasse).

## Acessando os itens do cardápio
Vamos criar um prato e uma bebida a partir de `app.py`:
```python
# Versão simplificada do arquivo `app.py`:
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')

print(bebida_suco)
print(prato_paozinho)
```
As classes herdarão corretamente da classe `ItemRestaurante` - embora essa classe não tenha sido diretamente importada em `app.py`. No entanto, o formato de string das classes `Bebida` e `Prato` não está legível. Para melhorar a legibilidade, vamos sobrescrever a função `__str__` dessas duas classes:
```python
from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio): # ou 
# class Prato(ItemCardapio):
    # Resto do código

    def __str__(self):
        return self._nome
```
# Polimorfismo e método abstrato
## Métodos para adicionar itens
Vamos criar métodos na classe `Restaurante` para acrescentas pratos e bebidas:

```python
# modelos/restaurante.py
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        # Resto do código
        self._cardapio = []
        # Resto do código

    def adicionar_bebida_no_cardapio(self, bebida):
        self._cardapio.append(bebida)

    def adicionar_prato_no_cardapio(self, prato):
        self._cardapio.append(prato)
```
## Refatoração
Na classe `Restaurante`, vamos unir os métodos `adicionar_bebida_no_cardapio` e `adicionar_prato_no_cardapio` em um único método que chamaremos de `adicionar_no_cardapio`:
```Python
# modelos/restaurante.py
from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        # Resto do código
        self._cardapio = []
        # Resto do código

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
```
> Note o uso da função `isinstance(obj, cls)` no novo método: isso serve para garantir que somente as classes filha de `ItemCardapio` podem ser inseridas no cardápio.

## Exibindo o cardápio
Implementação da função para exibir cardárpio na classe Restaurante: 

```python
# modelos/restaurante.py
# Resto do código
class Restaurante:
    # Resto do código

    def exibir_cardapio(self):
        print(f'Cardapio do restaurante "{self._nome}"\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                mensagem_prato = f"{i}. Nome: {item._nome} | Preço: R$ {item._preco:.2f} | Descrição: {item._descricao}"
                print(mensagem_prato)
            else:
                mensagem_bebida = f"{i}. Nome: {item._nome} | Preço: R$ {item._preco:.2f} | Tamanho: {item._tamanho}"
                print(mensagem_bebida)
```
Pontos de destaque: 

1. a função `enumerate` retorna dois valores: um índice do enumerável percorrido e o item enumerado. Essa função recebe o enumerável em si como primeiro parâmetro e o parâmetro opcional `start` (que representa o número do primeiro item listado);
2. a função `hasattr` testa se o objeto fornecido como parâmetro possui algum atributo com o nome fornecido como segundo parâmetro.

## Métodos abstrato
O Python usa a superclasse `ABC` para prover funcionalidades de classe abstrata - aquelas cujos objetos só podem ser instanciados se tiver subclasses com implementações específicas. 

Classes que herdam de `ABC` podem definir métodos abstratos (aqueles que não possuem implementação) com a anotação `abstractmethod`. Veja o código do arquivo da classe `ItemCardapio` como exemplo:

```python
# modelos/cardapio/item_cardapio.py
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    # Resto do código

    @abstractmethod
    def aplicar_desconto(self):
        pass
```

## Polimorfismo
A subclasse é obrigada a conter uma assinatura do método abstrato, mas isso não significa que o método precisa ser implementado de fato:

```python
# Exemplo fictício
class Sobremesa(ItemCardapio):
    # Resto do código
    def aplicar_desconto(self):
        pass
```

O conceito de polimorfismo significa que diferentes subclasses podem ter métodos com nomes iguais, mas com comportamentos diferentes (muitas formas = polimorfismo). Veja o exemplo das subclasses de `ItemCardapio`:

```python
# modelos/cardapio/prato.py
from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    # Resto do código

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)


# modelos/cardapio/bebida.py
from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    # Resto do código

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)
```
As classes `Prato` e `Bebida` tem o mesmo método `aplicar_desconto`, mas cada um tem uma forma/comportamento distinto.
