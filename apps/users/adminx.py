# -*- coding: utf-8 -*- 
__author__ = 'yank'
__date__ = '2018/6/28/20:57'

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSetting:
    # 主题功能开启,默认关闭
    enable_themes = True
    use_bootswatch = True


# 全局设置后台系统标题和底部信息
class GlobalSetting:
    site_title = "yank后台管理系统"
    site_footer = "小牛在线"
    # 菜单栏收起
    menu_style = "accordion"


class EmailVerifyRecordAdmin:
    # 定义xadmin后台显示的列,元组和列表都可以,推荐使用列表
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 定义搜索字段
    search_fields = ['code', 'email']
    # 过滤字段,生成过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin:
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']  # 时间搜索会报错
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# 将model与admin管理器进行关联注册
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

# 主题注册
xadmin.site.register(views.BaseAdminView, BaseSetting)

# 全局修改标题
xadmin.site.register(views.CommAdminView, GlobalSetting)
