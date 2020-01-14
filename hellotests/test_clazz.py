# -*- coding: utf-8 -*-
'''
@Date: 2020-01-13 23:06:04
@LastEditors  : fzzjj2008
@LastEditTime : 2020-01-14 08:35:25
'''
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
        mock_teacher.greet.return_value = '%s: greet_student'
        mock_student.greet.return_value = '%s: greet_teacher'
        clazz = Clazz(TEACHER, STU_LIST)
        clazz.tea = mock_teacher
        for student in clazz.stu:
            student = mock_student
        # 测试
        assert clazz.greet() == '李老师: greet_student\n张三：greet_teacher\李四：greet_teacher'

    @patch("hello.student.Student")
    def test_exam(self, mock_student):
        TEACHER = '李老师'
        STU_LIST = ['张三', '李四']
        SCORE_DICT = {'张三' : 66, '王五': 88}
        # mock替换函数
        def mock_print_score():
            level = ''
            if score >= 0 and score < 60:
                level = 'E'
            elif score >= 60 and score < 70:
                level = 'D'
            elif score >= 70 and score < 80:
                level = 'C'
            elif score >= 80 and score < 90:
                level = 'B'
            elif score >= 90 and score <= 100:
                level = 'A'
            return 'level: %s' % level

        clazz = Clazz(TEACHER, STU_LIST)
        for student in clazz.stu:
            student.print_score = mock_print_score
        # 测试
        assert clazz.exam(SCORE_DICT) == '张三 考试成绩：及格\n李四 '