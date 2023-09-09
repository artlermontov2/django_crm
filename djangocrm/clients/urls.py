from django.urls import path
from . import views


app_mame = 'clients'

urlpatterns = [
    path("add_client/", views.add_client, name="add_client"),
    path("view_client/<int:pk>/", views.view_client, name="view_client"),
    path("delete_client/<int:pk>/", views.del_client, name="del_client"),
    path("edit/<int:pk>/", views.update_info, name="update_info"),
    path("send/<int:id>/", views.send_message, name="send_message"),
    # path("edit/<int:pk>/", views.UpdateRecordView.as_view(), name="update_info")
]

