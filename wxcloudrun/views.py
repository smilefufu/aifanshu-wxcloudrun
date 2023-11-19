from datetime import datetime
from flask import render_template, request
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid
from wxcloudrun.model import Counters
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
from utils import find_last_number, get_reply_content


@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')


@app.route('/api/count', methods=['POST'])
def count():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    # 执行自增操作
    if action == 'inc':
        counter = query_counterbyid(1)
        if counter is None:
            counter = Counters()
            counter.id = 1
            counter.count = 1
            counter.created_at = datetime.now()
            counter.updated_at = datetime.now()
            insert_counter(counter)
        else:
            counter.id = 1
            counter.count += 1
            counter.updated_at = datetime.now()
            update_counterbyid(counter)
        return make_succ_response(counter.count)

    # 执行清0操作
    elif action == 'clear':
        delete_counterbyid(1)
        return make_succ_empty_response()

    # action参数错误
    else:
        return make_err_response('action参数错误')


@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """
    counter = Counters.query.filter(Counters.id == 1).first()
    return make_succ_response(0) if counter is None else make_succ_response(counter.count)


@app.route('/api/gzh_msg', methods=['POST'])
def gzh_msg():
    data = request.json
    to_uer_name = data['ToUserName']
    from_user_name = data['FromUserName']
    msg_type = data['MsgType']
    content = data['Content']
    create_time = data['CreateTime']
    if msg_type == 'text':
        # 解析数字
        number = find_last_number(content)
        if number is None:
            reply_txt = "公主：你想问的是什么数字呀，AI我没看懂呀"
        else:
            reply_txt = get_reply_content(number)
            if reply_txt is None:
                reply_txt = "公主：仅支持1-250哦"
        payload = {
            "ToUserName": from_user_name,
            "FromUserName": to_uer_name,
            "CreateTime": create_time,
            "MsgType": 'text',
            "Content": reply_txt
        }
        return make_succ_response(payload)
    return make_succ_empty_response()