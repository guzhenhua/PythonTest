import yaml


def get_test_data(test_data_path):
    case = []  # 存储测试用例名称
    http = []  # 存储请求对象
    expected = []  # 存储预期结果
    dat = yaml.safe_load(open(test_data_path,encoding='utf-8'))
    test = dat['tests']
    for td in test:
        case.append(td.get('case', ''))
        http.append(td.get('http', {}))
        expected.append(td.get('expected', {}))
    parameters = zip(case, http, expected)
    return case, parameters
# cases, parameters = get_test_data("../data/test_in_post.yaml")
# list_params=list(parameters)
#
# print(cases)
# print(list_params[0][1]["method"])
# print(list_params)