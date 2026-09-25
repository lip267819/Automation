import logging

import allure
import jsonpath

from utils.send_request import send_jdbc_request


def json_extractor(case,res,all,index=0):
    if case["jsonExData"]:
        with allure.step("4.JSON提取"):
            for key, value in eval(case["jsonExData"]).items():
                value = jsonpath.jsonpath(res.json(),value)[index]
                all[key] = value

            logging.info(f"JSON提取，根据（{case['jsonExData']}）提取数据，此时全局变量为：{all}")

def sql_extractor(case,all):
    if case["sqlExData"]:
        with allure.step("4.SQL提取"):
            for key, value in eval(case["sqlExData"]).items():
                value = send_jdbc_request(value)
                all[key] = value

            logging.info(f"4.SQL提取，根据（{case['sqlExData']}）提取数据，此时全局变量为：{all}")


