# API de Livros

**Ferramentas**
* Python
* Playwright
* Pycharm
* Allure Reports
* Json Schema Validator


## Configuração

instalar o BREW /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

dependencias:

sudo xcode-select --install (terminal) download https://www.python.org/downloads/ python3 --version curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py python3 get-pip.py pip install --upgrade pip brew install allure

https://www.java.com/pt-BR/download/help/mac_install.html

para instalar as dependencias pip install -r requirementes.txt

## documentação 


Rodar todos os testes:

```
pytest 
```
Rodar pela linha de comando exemplo:

```
pytest pytests/specs/test_delete_livraria.py 
```

Rodar pela linha de comando por tag exemplo:

```
pytest -m crud_livros
```

Rodar pela linha de comando com paralelismo:
```
pytest -m crud_livros
```

Rodar o servidor Allure 

```
allure serve report/allure-results
```
## Arquitetura

### Clients

centraliza a lógica de comunicação com a API, permitindo que os testes ou outros módulos do sistema interajam de maneira consistente com diferentes recursos da API sem duplicação de código

### Common: 
incorrect_payload: Retorna diferentes tipos de dados de acordo com a entrada.

values_change: Modifica ou gera valores baseados em padrões específicos.

change_fields_payload: Modifica um campo no payload, podendo lidar com campos de múltiplos níveis.

remove_fields_payload: Remove um campo do payload, tratando diferentes profundidades.

validate_response: Valida a resposta de uma requisição, verificando o código de status e registrando informações de log.

### Examples 

Contem vários arquivos que contém exemplos de dados inválidos para diferentes operações relacionadas à livraria. Cada arquivo pode conter uma lista de exemplos com um tipo de entrada inválida e o código de resposta esperado

### Mock 

Usada para armazenar dados simulados

### Schemas 

Usada para armazenar definições de esquemas de dados, como a estrutura de objetos JSON que são esperados nas requisições ou respostas da API

### Specs 

Usada para armazenar os testes

### Suports 

Usada para arquivos de configuracoes e globais


## Obs

site para converter em schema: https://www.liquid-technologies.com/online-json-to-schema-converter