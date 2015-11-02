from django.conf.urls import patterns, include, url

urlpatterns = patterns('todolist.views',
    url(r'^todolist/$','todolist',name='todolist'),
    url(r'^add_task/$','add_task',name='add_task'),
    url(r'^register_user/$','register_user',name='register_user'),
    url(r'^resolve_task/(?P<name>\w+)$','resolve_task',name='resolve_task'),
    url(r'^todolist/(?P<pk>[0-9]+)$','task_details',name='task_details')
)
