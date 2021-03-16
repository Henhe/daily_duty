from django.urls import path

from duty.views import index, commands, lines, staff, periods, dutyes
from duty.views import edit_command
# from duty.views import Commands_add_edit

urlpatterns = [
    path('', index, name="index"),

    path('commands/', commands, name="commands"),
    # path('<int:command_line_id>/', Commands_add_edit.as_view(), name='addcommands'),
    path('<int:command_line_id>/', edit_command, name='addcommands'),
    path('lines/', lines, name="lines"),
    path('staff/', staff, name="staff"),
    path('periods/', periods, name="periods"),
    path('dutyes/', dutyes, name="dutyes"),

]
