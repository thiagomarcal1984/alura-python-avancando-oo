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
