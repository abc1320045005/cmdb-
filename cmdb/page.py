from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2  # 每页 2 条数据
    page_size_query_param = 'page_size'
    page_query_param = 'p'  # 请求页码的参数名
    max_page_size = 2  
    def get_paginated_response(self, data):
      return Response({
          'links': self.get_html_context(),
          'count': self.page.paginator.count,
          'results': data
      })