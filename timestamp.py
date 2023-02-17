import time
import re
import json
import sys

# /usr/bin/php timestamp.php "{query}"

# 默认展示当天时间信息. `t `
# 也可以使用 `t tomorrow` `t yesterday`.
# 将时间戳转换成日期格式, 反之亦然 `t 1495276608` `t 2017-05-20 18:52:46`.
# 选中某一项转换结果键入 Enter 即可复制, Shift + Enter 将发音.

iconPngUrl = 'icon.png'


def outputs_format(query, valid=True):
    time_struct = time.localtime(query)
    date = time.strftime('%Y-%m-%d', time_struct)
    timee = time.strftime('%Y-%m-%d %X', time_struct)

    outputs = {
        'items': [{
            'arg': query,
            'title': query,
            'subtitle': 'Timestamp - 时间戳',
            'icon': {
                'path': iconPngUrl
            },
            'valid': valid,
        }, {
            'arg': date,
            'title': date,
            'subtitle': 'Date - 日期',
            'icon': {
                'path': iconPngUrl
            },
            'valid': valid,
        }, {
            'arg': timee,
            'title': timee,
            'subtitle': 'Date/time - 日期时间',
            'icon': {
                'path': iconPngUrl
            },
            'valid': valid,
        }]
    }
    return json.dumps(outputs, ensure_ascii=False)


def strtotime(string):
    string = string.strip()

    # 解析时间戳
    if re.match(r'(\d{10})(.\d+)?', string):
        return float(''.join(re.findall(r'\d+', string)))

    # 解析时间日期
    re_res = re.findall('\d+', string)
    if re_res and len(re_res) >= 3:
        if len(re_res) < 6:
            for i in range(6 - len(re_res)):
                re_res.append('0')
        timeArray = time.strptime(','.join(re_res), "%Y,%m,%d,%H,%M,%S")
        return time.mktime(timeArray)

    unit_to_second = dict(minute=60,
                          hour=3600,
                          day=86400,
                          week=604800,
                          year=(365 * 86400) + 86400)

    accumulator = time.time()
    delta = 0
    plus = True
    if (string == 'today') or (string == 'yesterday') or (
            'midnight' in string) or ('this month' in string):
        time_struct = time.localtime(accumulator)
        timestr_day = time.strftime('%Y:%m:%d %X', time_struct)
        year, month, day, hour, minute, second = re.findall(
            r'\d+', timestr_day)
        accumulator -= int(second)
        accumulator -= int(minute) * unit_to_second['minute']
        accumulator -= int(hour) * unit_to_second['hour']
    if string == 'this month':
        day = int(day) - 1
        string = '-' + str(day) + ' day'
    if 'yesterday' in string:
        string = '-1 day'
    if string == 'the day before yesterday':
        string = '-2 days'
    if string.startswith('in ') > 0:
        string = string.replace('in ', '', 1)
        pass
    if string.startswith('+') > 0:
        string = string.strip('+')
        pass
    if string.startswith('-'):
        plus = False
        string = string.strip('-')
    if 'ago' in string:
        plus = False
        string = string.replace(' ago', '', 1)
    string = string.strip()
    for match in re.finditer(r"(\d+) (minute|hour|day|week|year)", string):
        num, unit = match.groups()
        delta += float(num) * unit_to_second[unit]
    if plus:
        accumulator += delta
    else:
        accumulator -= delta
    return accumulator


if __name__ == '__main__':
    key_list = sys.argv
    if (len(key_list) <= 1) or key_list[1] in ['n', 'now']:
        query = time.time()
        print(outputs_format(query))
    else:
        querys = ' '.join(key_list[1:])
        print(outputs_format(strtotime(querys)))
        # else:
        #     outputs = {
        #         'items': [{
        #             'uid': '时间格式输入有误',
        #             'arg': '',
        #             'title': '请输入时间戳或日期格式',
        #             'subtitle':
        #             '日期/时间字符串 - Power by PHP strtotime Date/Time 函数.',
        #             'icon': {
        #                 'path': iconPngUrl
        #             },
        #             'valid': False
        #         }]
        #     }
