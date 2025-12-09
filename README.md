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
