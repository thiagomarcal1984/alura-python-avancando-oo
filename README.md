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
        
# modelos/cardapio/prato.py
class Bebida:
    def __init__(self, nome, preco, tamanho):
        pass
```
Por ora, a relação de herança não foi estabelecida. Na próxima aula isso será realizado.
