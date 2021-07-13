'''创建一个类来继承自定义的配置
'''
from rest_framework.pagination import PageNumberPagination
class MyGageSet(PageNumberPagination):
    '''自定义分页'''
    page_size = 10 #每页多少个数据
    page_size_query_param = 'page_size'
    max_page_size = 10

