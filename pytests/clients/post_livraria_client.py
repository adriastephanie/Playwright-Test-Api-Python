from playwright.sync_api import sync_playwright
from pytests.support.api_utils import ApiUtils
from pytests.support.hooks import *
import os

class PostLivrariaClient:
    @staticmethod
    def post_livros(payload):
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.post(f"{os.environ['BASE_URL']}", data=payload)
            LOG.log_info("POST")
            LOG.log_info(f"URL: {os.environ['BASE_URL']}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    @staticmethod
    def validate_response(response, code):
        ApiUtils.resquest_parse_log(response)
        ApiUtils.validate_status_code(response, code)