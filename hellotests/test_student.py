# -*- coding: utf-8 -*-
'''
@Date: 2020-01-14 07:21:23
@LastEditors  : fzzjj2008
@LastEditTime : 2020-01-14 07:39:59
'''

import pytest
from hello.student import Teacher, Student

class TestStudent:
    
    def test_teacher_greet(self):
        TEACHER = '李老师'
        tea = Teacher(TEACHER)
        assert tea.name == TEACHER
        assert tea.greet() == '李老师：同学们好\n'

    def test_student_greet(self):
        STUDENT = '小明'
        stu = Student(STUDENT)
        assert stu.name == STUDENT
        assert stu.greet() == '小明：老师好\n'

    def test_student_score(self):
        STUDENT = '小明'
        SCORE = 99
        stu = Student(STUDENT)
        assert stu.name == STUDENT
        assert stu.score == 0
        stu.set_score(SCORE)
        assert stu.score == SCORE
        assert stu.print_score() == '小明 考试成绩：99\n'
    
    def test_student_score_err(self):
        STUDENT = '小明'
        SCORE = -1
        stu = Student(STUDENT)
        assert stu.name == STUDENT
        assert stu.score == 0
        stu.set_score(SCORE)
        assert stu.score == SCORE
        assert stu.print_score() == AttributeError('输入错误')
