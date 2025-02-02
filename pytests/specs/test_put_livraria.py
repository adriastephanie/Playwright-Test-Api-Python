import pytest
from pytests.support.hooks import *
from pytests.mocks.livraria_mock import *
from pytests.clients.put_livraria_client import PutLivrariaClient
from pytests.support.api_utils import ApiUtils
from pytests.schemas.put_livraria_schema import *
from pytests.clients.common import Commom

# teste funcional da rota e verifica o contrato
@pytest.mark.crud_livros
def test_put_livro():
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    response = PutLivrariaClient.put_livros(payload, 1869)
    Commom.validate_response(response, 200)
    ApiUtils.validate_schema(response, put_schema)