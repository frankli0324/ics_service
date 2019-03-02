import requests
import re
import variables
import json
import os
import random
import hashlib
import time

random.seed(time.time_ns())


def _check_empty(x):
    for i in x:
        if(len(i) > 0):
            return False
    return True


def get_login_session(target, username, password):
    ses = requests.session()
    ses.headers = variables.HEADER
    page = ses.get(
        'http://ids.xidian.edu.cn/authserver/login',
        params={'service': target}
    ).text
    page = re.sub(variables.REGEX_HTML_COMMENT, '', page)
    params = {i[0]: i[1] for i in re.findall(variables.REGEX_HIDDEN_TAG, page)}
    ses.post(
        'http://ids.xidian.edu.cn/authserver/login',
        params={'service': target},
        data=dict(params, **{
            'username': username,
            'password': password
        })
    )
    return ses


def courses_from_ehall(username, password, semester=None, force=False):
    courseList = []
    # 换校历的话可能要改, 不换就没事
    ses = get_login_session(
        'http://ehall.xidian.edu.cn:80//appShow',
        username,
        password
    )
    if '<input id="username" name="username" placeholder="用户名" class="auth_input"' in ses.get('http://ehall.xidian.edu.cn//appShow?appId=4770397878132218', headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    }).text:
        return False

    semesterCode = ses.post(
        'http://ehall.xidian.edu.cn/jwapp/sys/wdkb/modules/jshkcb/dqxnxq.do',
        headers={
            'Accept': 'application/json, text/javascript, */*; q=0.01'
        }
    ).json()['datas']['dqxnxq']['rows']

    if semester in [x['DM'] for x in semesterCode]:
        semesterCode = semester
    else:
        semesterCode = semesterCode[0]['DM']

    if (force == False) and os.path.exists('./users/'+username+'-'+semesterCode):
        f = open('./users/'+username+'-'+semesterCode)
        s = f.read()
        f.close()
        return s
    ##########already got in disk#############

    qResult = ses.post(
        'http://ehall.xidian.edu.cn/jwapp/sys/wdkb/modules/xskcb/xskcb.do',
        headers={  # 学生课程表
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01'
        }, data={
            'XNXQDM': semesterCode
        }
    ).json()
    qResult = qResult['datas']['xskcb']  # 学生课程表
    if qResult['extParams']['code'] != 1:
        raise Exception(qResult['extParams']['msg'])

    for i in qResult['rows']:
        while len(courseList) < len(i['SKZC']):
            courseList.append([[], [], [], [], [], [], []])
        for j in range(len(i['SKZC'])):
            if i['SKZC'][j] == '1':
                courseList[j][int(i['SKXQ'])-1].append({
                    'name': i['KCM'],
                    'location': i['JASMC'],
                    'sectionSpan': (int(i['KSJC']), int(i['JSJC']))
                })

    while _check_empty(courseList[-1]):
        courseList.pop()

    filename = username+'-'+semesterCode
    uuid = hashlib.sha256(
        (filename+str(random.randint(0, 20000))).encode('utf-8')).hexdigest()
    f = open('./users/'+filename, 'w')
    f.write(uuid)
    f.close()
    f = open('./data/'+uuid, 'w')
    f.write(json.dumps(courseList))
    f.close()
    return uuid
