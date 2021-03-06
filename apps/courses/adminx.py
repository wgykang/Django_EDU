# -*- coding: utf-8 -*- 
__author__ = 'yank'
__date__ = '2018/6/28/20:57'

import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin:
    list_display = ['name','desc','detail','degree','learn_times','students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name','desc','detail','degree','learn_times','students']
    # 富文本
    style_fields = {"detail": "ueditor"}


class LessonAdmin:
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    # __name代表使用外键中name字段
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin:
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin:
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'download', 'add_time']


# 将管理器与model进行注册关联
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
