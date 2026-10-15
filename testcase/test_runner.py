import logging

from jinja2 import Template

import pytest

from utils.allure_utils import allure_init
from utils.analyse_case import analyse_case
from utils.asserts import http_assert, jdbc_assert
from utils.excel_utils import get_workbook
from utils.extractor import json_extractor, sql_extractor
from utils.send_request import send_http_request


class TestRunner:

    data = get_workbook()

    all = {}

    @pytest.mark.parametrize('case',data)
    def test_case(self,case):

        all = self.all

        case = eval(Template(str(case)).render(all))

        allure_init(case)

        logging.info(f"0.用例ID:{case['id']} 模块:{case['feature']} 场景:{case['story']} 标题:{case['title']}")


        request_data = analyse_case(case)

        res = send_http_request(request_data)

        http_assert(case,res)
        jdbc_assert(case)

        json_extractor(case,res,all)
        sql_extractor(case,all)
