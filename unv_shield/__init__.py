import json
import random
import logging
import azure.functions as func

from .handler import 生, 死


def 相位转移(tp, x):
    try:
        return tp(x)
    except Exception:
        return x


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        参数表 = 提取参数(req)
        参数新表 = {}
        for k, v in 参数表.items():
            tp = 生.__annotations__.get(k, float)
            参数新表[k] = 相位转移(tp, v)
        return func.HttpResponse(
            死(**参数新表), 
            mimetype='image/svg+xml', 
            headers={'Cache-Control': f'max-age={random.randint(60*10, 60*120)}'},
        )
    except Exception as e:
        logging.exception(e)
        return response(f'运行错误: {repr(e)}', status_code=422)


def response(x, status_code=200):
    新x = json.dumps(x, ensure_ascii=False)
    return func.HttpResponse(新x, status_code=status_code)


def 提取参数(req: func.HttpRequest) -> dict:
    参数表 = dict(req.params)
    try:
        req_body = req.get_json()
    except ValueError:
        for i, x in req.form.items():
            参数表[i] = json.loads(x)
    else:
        参数表.update(req_body)
    参数表.pop('code', '')
    参数表.pop('clientId', '')
    return 参数表
