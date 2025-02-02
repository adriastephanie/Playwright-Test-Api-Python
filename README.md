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

Rodar o servidor Allure 

```
allure serve report/allure-results
```

### Common: 
incorrect_payload: Retorna diferentes tipos de dados de acordo com a entrada.

values_change: Modifica ou gera valores baseados em padrões específicos.

change_fields_payload: Modifica um campo no payload, podendo lidar com campos de múltiplos níveis.

remove_fields_payload: Remove um campo do payload, tratando diferentes profundidades.

validate_response: Valida a resposta de uma requisição, verificando o código de status e registrando informações de log.