from http.client import responses

import pytest

from pytests.clients.common import Commom
from pytests.examples.examples_test_get_livraria import examples_get_livraria_invalid_values
from pytests.support.hooks import *
from pytests.clients.get_livraria_client import GetLivrariaClient
from pytests.support.api_utils import ApiUtils
from pytests.schemas.get_livraria_schema import get_schema
from pytests.examples.examples_test_post_livraria import *

# teste funcional + contrato sem passar id
@pytest.mark.crud_livros
def test_get_all_livro():
    response = GetLivrariaClient.get_livros()
    Commom.validate_response(response, 200)

# teste funcional passando id
@pytest.mark.crud_livros
def test_get_id_livro():
    response = GetLivrariaClient.get_livros(2150)
    Commom.validate_response(response, 200)
    ApiUtils.validate_schema(response, get_schema)

# teste dos valores invalidos do get
@pytest.mark.crud_livros
@pytest.mark.parametrize("value, code", examples_get_livraria_invalid_values)
def test_get_livro_invalid_values(value, code):
    value_change = Commom.values_change(value)
    response = GetLivrariaClient.get_livros(value_change)
    Commom.validate_response(response, code)