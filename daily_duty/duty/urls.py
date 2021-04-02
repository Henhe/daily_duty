from django.urls import path

from duty.views import index, commands, lines, periods, dutyes, workhours, employees
from duty.views import edit_common


urlpatterns = [
    path('', index, name="index"),
    # path('<str:table_name>/<wh_id>/<str:_mode>/<h_id>/', input_time_workinghours, name='date_workinghours'),
    path('<str:table_name>/<_id>/<str:_mode>/', edit_common, name='view_list'),
    path('commands/', commands, name="commands"),
    path('lines/', lines, name="lines"),
    # path('<int:line_id>/<str:line_mode>/', edit_line, name='addlines'),
    path('employees/', employees, name="employees"),
    path('periods/', periods, name="periods"),
    path('workhours/', workhours, name="workhours"),
    path('dutyes/', dutyes, name="dutyes"),

]
