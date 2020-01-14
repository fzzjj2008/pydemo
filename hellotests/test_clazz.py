# -*- coding: utf-8 -*-
'''
@Date: 2020-01-13 23:06:04
@LastEditors  : fzzjj2008
@LastEditTime : 2020-01-14 08:35:25
'''
import sys, os
sys.path.append(os.getcwd())
import pytest
from unittest.mock import patch, Mock
from hello.clazz import Clazz
from hello.student import Teacher, Student

class TestClazz:

    @patch("hello.student.Student")
    @patch("hello.student.Teacher")
    def test_greet(self, mock_teacher, mock_student):
        # 造数据
        TEACHER = '李老师'
        STU_LIST = ['张三', '李四']
        # mock替换函数
        mock_teacher.greet.return_value = 'greet_student\n'
        mock_student.greet.return_value = 'greet_teacher\n'
        clazz = Clazz(TEACHER, STU_LIST)
        clazz.tea = mock_teacher
        for index in range(len(clazz.stu)):
            clazz.stu[index] = mock_student
        # 测试
        assert clazz.greet() == 'greet_student\ngreet_teacher\ngreet_teacher\n'

    @patch.object(Student, "print_score")
    def test_exam(self, mock_score):
        TEACHER = '李老师'
        STU_LIST = ['张三', '李四']
        SCORE_DICT = {'张三' : 66, '李四': 66}
        # mock替换函数
        mock_score.return_value = '及格'
        clazz = Clazz(TEACHER, STU_LIST)
        for index in range(len(clazz.stu)):
            clazz.stu[index].print_score = mock_score
        # 测试
        ret = clazz.exam(SCORE_DICT)
        assert ret == '及格及格'
