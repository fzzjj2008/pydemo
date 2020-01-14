# -*- coding: utf-8 -*-
'''
@Date: 2020-01-12 23:39:15
@LastEditors  : fzzjj2008
@LastEditTime : 2020-01-14 07:34:11
'''
from hello.student import Teacher, Student

class Clazz:

    def __init__(self, tea_name, stu_list):
        self.tea = Teacher(tea_name)
        self.stu = []
        for stu_name in stu_list:
            self.stu.append(Student(stu_name))

    def greet(self):      
        greet_content = ''  
        greet_content += self.tea.greet()
        for student in self.stu:
            greet_content += student.greet()
        return greet_content

    def exam(self, score_dict):
        exam_content = ''
        for student in self.stu:
            if student.name in score_dict:
                student.set_score(score_dict[student.name])
        for student in self.stu:
            exam_content += student.print_score()
        return exam_content
