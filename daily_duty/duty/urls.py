from django.urls import path

from duty.views import commands, lines, periods, dutyes, workhours, employees
from duty.views import edit_common, get_info, register, fill_duty
from duty.views import api_commandsline, api_duty_data
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', get_info, name="index"),
    path('api/commands/<str:_type_duty>/<int:_day>/<int:_month>/<int:_year>/', api_duty_data),
    path('api/commands/', api_commandsline),

    path('indexView/', get_info, name="indexView"),
    path('fillduty/', fill_duty, name="fillduty"),
    # path('accounts/logout/', auth_views.LogoutView.as_view()),
    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', register, name='register'),
    # path('index', DutyesCommonView.as_view(), name="index"),
    path('index', get_info, name="index"),
    # path('index/<_id>/', index_view, name="index_view"),
    # path('<str:table_name>/<wh_id>/<str:_mode>/<h_id>/', input_time_workinghours, name='date_workinghours'),
    path('<str:table_name>/<_id>/<str:_mode>/<str:return_to_index>/', edit_common, name='view_list'),
    path('<str:table_name>/<_id>/<str:_mode>/', edit_common, name='view_list'),
    path('commands/', commands, name="commands"),
    path('lines/', lines, name="lines"),
    # path('<int:line_id>/<str:line_mode>/', edit_line, name='addlines'),
    path('employees/', employees, name="employees"),
    path('periods/', periods, name="periods"),
    path('workhours/', workhours, name="workhours"),
    path('dutyes/', dutyes, name="dutyes"),

]
