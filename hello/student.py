# -*- coding: utf-8 -*-
'''
@Date: 2020-01-12 23:39:27
@LastEditors  : fzzjj2008
@LastEditTime : 2020-01-14 07:35:23
'''

from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    @abstractmethod
    def talk(self, msg):
        raise NotImplementedError()


class Teacher(Person):

    def __init__(self, name):
        self.name = name

    def talk(self, msg):
        return ('%s：%s\n' % (self.name, msg))

    def greet(self):
        return self.talk('同学们好')


class Student(Person):

    def __init__(self, name):
        self.name = name
        self.score = 0

    def talk(self, msg):
        return ('%s：%s\n' % (self.name, msg))

    def greet(self):
        return self.talk('老师好')

    def set_score(self, score):
        self.score = score

    def print_score(self):
        if self.score >= 0 and self.score < 60:
            level = '不及格'
        elif self.score >= 60 and self.score < 70:
            level = '及格'
        elif self.score >= 70 and self.score < 80:
            level = '中'
        elif self.score >= 80 and self.score < 90:
            level = '良'
        elif self.score >= 90 and self.score <= 100:
            level = '优'
        else:
            raise AttributeError('输入错误')
        return ('%s 考试成绩：%s\n' % (self.name, level))
