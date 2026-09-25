import os

import pytest

if __name__ == '__main__':
    pytest.main([
        '-vs',
        './testcase/test_runner.py',
        '--alluredir',
        './reports/json_report',
        '--clean-alluredir'
    ])
    os.system('allure generate ./reports/json_report -o ./reports/html_report --clean')
    # os.system('allure open ./reports/html_report')