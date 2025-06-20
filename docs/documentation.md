# Documentação da API FastAPI

O código a seguir é uma implementação simples de uma API de gerenciamento de itens usando FastAPI. Ele permite criar, ler e atualizar itens.

## Dependências

- FastAPI
- Pydantic

## Data Model

`Item` é uma classe que representa um item com as seguintes propriedades:

- `name`: (string) - o nome do item.
- `description`: (string, opcional) - uma descrição opcional do item.
- `price`: (float) - o preço do item.

## Endpoints

### POST /items/

Cria um novo item.

#### Parâmetros

- `item` (Item): Um objeto Item para ser adicionado à lista de itens.

#### Exemplo de uso:

```python
import requests
import json

item = {
    "name": "Item1",
    "description": "This is Item1",
    "price": 9.99
}

response = requests.post("http://localhost:8000/items/", data=json.dumps(item))
```

### GET /items/{item_id}

Obtém um item pela ID.

#### Parâmetros

- `item_id` (int): A ID do item a ser obtido.

#### Exemplo de uso:

```python
import requests

response = requests.get("http://localhost:8000/items/1")
```

### PATCH /items/{item_id}

Atualiza um item pela ID.

#### Parâmetros

- `item_id` (int): A ID do item a ser atualizado.
- `item` (Item): Um objeto Item com os novos dados.

#### Exemplo de uso:

```python
import requests
import json

item = {
    "name": "Item1 Updated",
    "description": "This is Item1 Updated",
    "price": 19.99
}

response = requests.patch("http://localhost:8000/items/1", data=json.dumps(item))
```

## Notas Importantes

- As IDs dos itens são baseadas em zero, portanto, para obter ou atualizar o primeiro item, use a ID 0. 
- Se tentar obter ou atualizar um item com uma ID que não existe, a API retornará um erro HTTP 404. 

Portanto, é crucial garantir que a ID fornecida esteja correta e que o item exista.