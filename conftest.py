import logging

import pymysql
import pytest

from config.config import SQL1, SQL2, SQL3, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME


@pytest.fixture(scope="session", autouse=True)
def destroy_data():

    yield

    sqls = [
        SQL1,
        SQL2
    ]
    try:
        with pymysql.connect(
            host = DB_HOST,
            port = DB_PORT,
            user = DB_USER,
            password = DB_PASSWORD,
            database = DB_NAME,
            charset = "utf8mb4"
        ) as conn:
            with conn.cursor() as cur:
                affect_row = 0
                for sql in sqls:
                    row = cur.execute(sql)
                    affect_row += row
                    logging.info(f"执行SQL语句：{sql}，影响行数：{row}")
                conn.commit()
                logging.info(f"数据库清理完毕，影响总行数：{affect_row}")
    except Exception as e:
        logging.error(f"清理数据库失败，错误信息：{e}")
        raise