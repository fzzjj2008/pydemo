# -*- coding: utf-8 -*-
'''
@Date: 2019-12-22 18:18:00
@LastEditors  : fzzjj2008
@LastEditTime : 2020-01-14 07:34:43
'''

from hello.clazz import Clazz

if __name__ == "__main__":
    TEACHER = '李老师'
    STU_LIST = ['张三', '李四', '王五']
    SCORE_DICT = {'张三': 70, '王五': 100}
    CLAZZ1 = Clazz(TEACHER, STU_LIST)
    print(CLAZZ1.greet())
    print(CLAZZ1.exam(SCORE_DICT))
