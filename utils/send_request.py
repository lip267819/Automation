import logging

import allure
import pymysql
import requests

from config.config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME


@allure.step("2.发送HTTP请求")
def send_http_request(request_data):
    res = requests.request(**request_data)
    logging.info(f"2.发送HTTP请求，响应文本为：{res.text}")
    return res


def send_jdbc_request(sql, index=0):
    try:
        with pymysql.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME,
                charset="utf8mb4"
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                res = cur.fetchone()
                if res is None:
                    logging.warning(f"数据库查询无结果，SQL：{sql}")
                    return None
                return res[index]
    except Exception as e:
        logging.error(f"数据库查询失败！SQL：{sql}，错误：{e}")
        raise
