import requests
import pytest
from utils.commonlib import get_test_data

cases, list_params = get_test_data("./data/test_in_post.yaml")

class TestInPost(object):
    @pytest.mark.parametrize("case,http,expected",list(list_params), ids=cases)
    def test_in_post(self,preparation,env,case, http, expected):
        # host = "http://jsonplaceholder.typicode.com"
        r = requests.request(http["method"],
                             url=env["host"]["jsonplaceholder"] + http["path"],
                             headers=http["headers"],
                             json=http["body"])
        response = r.json()
        assert response["title"] == expected['response']["title"]
        assert response["body"] == expected['response']["body"]
        assert response["userId"] == expected['response']["userId"], "实际的标题是：{}".format(response["title"])

    @pytest.fixture(scope="function")
    def preparation(self):
        print("在数据库中准备测试数据")
        test_data = "在数据库中准备测试数据"
        yield test_data
        print("清理测试数据")