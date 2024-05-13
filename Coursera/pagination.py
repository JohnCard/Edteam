from rest_framework.pagination import PageNumberPagination,CursorPagination

class CoursePagination(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 5
    last_page_strings = 'end'

class CourseCPagination(CursorPagination):
    page_size = 4

class TeacherPagination(CursorPagination):
    page_size = 4