from playwright.sync_api import sync_playwright
from pytests.clients.common import Commom
from pytests.mocks.livraria_mock import payload_post_livros
from pytests.support.hooks import *
import os

class GetLivrariaClient:
    @staticmethod
    def get_livros(id=""):
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.get(f"{os.environ['BASE_URL']}/{id}")
            LOG.log_info("GET")
            LOG.log_info(f"URL: {os.environ['BASE_URL']}/{id}")
            return {"code": response.status, "body": response.text(), "headers": response.headers}