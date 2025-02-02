import pytest

from pytests.schemas.post_livro_schema import post_schema
from pytests.support.hooks import *
from pytests.mocks.livraria_mock import *
from pytests.clients.post_livraria_client import PostLivrariaClient
from pytests.support.api_utils import ApiUtils
from pytests.schemas import *

@pytest.mark.crud_livros
def test_post_livro():
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    response = PostLivrariaClient.post_livros(payload)
    PostLivrariaClient.validate_response(response, 201)
    ApiUtils.validate_schema(response, post_schema)
