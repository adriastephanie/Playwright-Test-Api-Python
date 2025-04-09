from pytests.schemas.delete_livraria_schema import delete_schema
from pytests.support.hooks import *
from pytests.mocks.livraria_mock import *
from pytests.clients.post_livraria_client import PostLivrariaClient
from pytests.support.api_utils import ApiUtils
from pytests.clients.common import Commom
from pytests.clients.delete_livraria_client import DeleteLivrariaClient
import json

def test_delete_livro():
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    response = PostLivrariaClient.post_livros(payload)
    Commom.validate_response(response, 201)
    response_json = json.loads(response['body'])
    id = response_json['id']
    response = DeleteLivrariaClient.delete_livros(id)
    Commom.validate_response(response, 200)
    ApiUtils.validate_schema(response, delete_schema)