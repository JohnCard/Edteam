from rest_framework.pagination import PageNumberPagination, CursorPagination

class CoursePagination(PageNumberPagination):
    # Page size
    page_size = 100
    # Allow us to specify how many we want on every page
    page_size_query_param = 'count'
    # How many it can take
    max_page_size = 200
    # Page query parameter name
    page_query_param = 'page'

class CourseCursorPagination(CursorPagination):
    page_size = 4

class TeacherPagination(CursorPagination):
    page_size = 4