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

# Ambientes virtuais
## Venv - Ambiente Virtual Python
Comando para criação do ambiente virtual:
```bash
python -m venv nome_do_ambiente
```
Os diretórios do ambiente virtual são: 
- include: local onde se guardam os cabeçalhos dos ambientes entre os módulos (cabeçalhos da linguagem C);
- Lib: contém os módulos Python (instalados via `pip`);
- Scripts (ou bin, no ambiente Linux): guarda os executáveis usados pelo ambiente virtual.
- pyvenv.cfg: guarda informações do ambiente (versão do Python, diretório do executável etc.)

Para ativar o ambiente virtual, usamos o script `activate`:

```bash
.\venv\Scripts\activate
```
ou no Linux/Mac: 
```bash
source venv/bin/activate
```

Perceba que ao lado do prompt vai aparecer o nome do ambiente virtual entre parênteses. 

Para desativar o ambiente virtual, use o script `deactivate`.

## Criando o Requirements.txt
Para instalar um pacote Python específico, use o instalador de pacotes pip. Vamos instalar, por exemplo, o módulo `requests`.

```bash
pip install requests
```

O comando `pip freeze` mostra as dependências instaladas via pip. Para criar um arquivo de texto com as dependências listadas com `pip freeze`, use uma saída de linha de comando para um arquivo txt: 

```bash
pip freeze > requirements.txt
```

É possível instalar módulos a partir de um arquivo de texto, geralmente nomeado como `requirements.txt`. Use a flag `-r` antes do nome do arquivo que vai conter as dependências:

```bash
pip install -r requirements.txt  
```
# Requisições, JSON e arquivos
## Requisição
Reescrevendo o arquivo `app.py` para usar a biblioteca `requests`:
```python
import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

print(response)

if response.status_code == 200:
    dados_json = response.json()
    print(dados_json)
else:
    print(f'O erro foi {response.status_code}.')
```
1. A biblioteca `requests` tem métodos para os verbos HTTP (incluindo o `get`), que retorna uma resposta/response;
2. A resposta tem várias propriedades, inclusive o status code (200 para OK ou 404 para não encontrado, dentre outros) e o conteúdo da resposta no formato JSON (usando o método `json` do objeto da resposta).

## Filtrando dados
```python
import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

print(response)

if response.status_code == 200:
    # Resposta em JSON.
    dados_json = response.json()

    # Dicionário cuja chave é o nome do restaurante 
    # e o valor é a lista com os dados do restaurante.
    dados_restaurante = {}

    for item in dados_json:
        nome_do_restaurante = item['Company']

        # Se o restaurante não possuir chave no dicionário, 
        # é criada uma nova lista associada a essa chave.
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        # Guarda os dados do restaurante na lista associada
        # à chave do restaurante.
        dados_restaurante[nome_do_restaurante].append({
            "item" : item['Item'],
            "price" : item['price'],
            "description" : item['description'],
        })
else:
    print(f'O erro foi {response.status_code}.')

# Filtrando apenas os items de restaurante pelo nome do restaurante.
print(dados_restaurante['McDonald’s'])
```

## Criando arquivos com Python
Para criar arquivos com Python, use o comando com esta sintaxe:
```python
# O parâmetro `w` indica permissão para escrita.
open(nome_arquivo, 'w')
```

Você pode usar um contexto para abrir e fechar o arquivo usando o comando `with`.
```python
import json
# Resto do código
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo =f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
```
Para escrever dados em formato JSON num arquivo, use a biblioteca `json` e sua função `dump`. Os parâmetros são os dados para escrita e o arquivo (não o nome do arquivo). O parâmetro `indent` é opcional e indica a indentação padrão para cada nível no JSON.

# FastAPI
## Usando o FastAPI
Primeiramente vamos instalar o FastAPI:

```bash
pip install fastapi uvicorn
```
O uvicorn provê um servidor de aplicações onde o FastAPI vai rodar.

Vamos atualizar o arquivo `requirements.txt`:
```bash
pip freeze > requirements.txt
```

Segue a implementação básica do FastAPI:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hello")
def hello_world():
    return {"Hello": "World"}
```
> Note a semelhança com a sintaxe do Flask: o objeto `app` contém um método `get` que é usado como anotação da função `hello_world`. O retorno é um dicionário - que acaba virando um JSON.


Para rodar a aplicação, use o comando abaixo do `uvicorn`:
```bash
uvicorn main:app --reload
```
> `main` é o nome do módulo; `app` é o nome do objeto do FastAPI que conterá as rotas.

Depois de rodar o comando com o `uvicorn`, acesse o endpoint criado (no caso seria http://127.0.0.1:8000/api/hello).

## Criando um endpoint
Código: 
```python
from fastapi import FastAPI, Query
import requests

app = FastAPI()

# Resto do código 

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return dados_json
        dados_restaurante = []
        for item in dados_json:
            if item['Company'].lower() == restaurante.lower():
                dados_restaurante.append({
                    "item" : item['Item'],
                    "price" : item['price'],
                    "description" : item['description'],
                })
        return {'Restaurante' : restaurante, 'Dados': dados_restaurante}
    else:
        return {"Erro": f"{response.status_code} - {response.text}"}
```
Testando a aplicação rapidamente, a rota para um restaurante específico não funciona, mas a rota geral funciona.

## Consultando um endpoint
O teste anterior falhou porque fornecemos uma URL sem variáveis de URL precedidas de sinal de interrogação.

Por exemplo: para visualizarmos os itens de cardápio do restaurante KFC, usamos a seguinte URL: http://127.0.0.1:8000/api/restaurantes/?restaurante=KFC . Note que depois do endpoint acrescentamos um `?restaurante=KFC`. Note também que o nome da variável `restaurante` na URL é o mesmo que é fornecido como parâmetro para a função `get_restaurantes` e que usa como tipo uma `Query(None)`.

Existe uma rota no FastAPI que serve como documentação da API: http://127.0.0.1:8000/docs . O endpoint `docs` mostra os endpoints que há na API e suas respectivas docstrings.

Exemplo de enpdoint com docstring:

```python
from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/api/hello")
def hello_world():
    '''
    Endpoint que exibe uma mensagem de boas-vindas.
    '''
    return {"Hello": "World"}
```
