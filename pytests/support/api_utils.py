from http.client import responses

from pytests.support.hooks import *
from jsonschema import validate
import json

class ApiUtils:
    @staticmethod
    def validate_status_code(request, code):
        @staticmethod
        def validate_status_code(request, code):
            try:
                LOG.log_info(f"Status code Esperado: {code}")
                LOG.log_info(f"Status code Recebido: {request['code']}")
                assert request['code'] == code
            except Exception as e:
                LOG.log_error("Erro ao validar status code!")
                raise e
    @staticmethod
    def resquest_parse_log(request):
        if "{" in request['body']:
            load = json.loads(request['body'])
            resp = json.dumps(load, indent=1, ensure_ascii=False)
            LOG.log_info(f"Response:\n{resp}")
            return load
        else:
            LOG.log_info(f"Response:\n{request['body']}")
            return request['body']

    @staticmethod
    def payload_parse(payload):
        resp = json.dumps(payload, indent=1, ensure_ascii=False)
        LOG.log_info(f"Payload:\n{resp}")

    @staticmethod
    def validate_schema(request, schema):
        try:
            response_json = json.loads(request['body'])
            validate(instance=response_json, schema=schema)
            LOG.log_info("contrato validado com sucesso!")
        except Exception as e:
            LOG.log_error("Erro ao validar contrato!")
            raise e
