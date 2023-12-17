from django.urls import path
from .views import (bulk_update_db,Project_page,Project_dashdata,search_district,project_fields,
                    search_result,project_rby_id,pro_files,modify_project,project_delete,department_update,
                    updated_project_list,upd_project_rby_id,pmu_approval,pmu_decline,
                    media_project_id,media_upload,video_doc_upload,media_delete)
urlpatterns = [
    path('add-csv',bulk_update_db,name="bulk add db"),
    path('project',Project_page.as_view(),name='project pagination'),
    path('dash',Project_dashdata,name='dashboard data'),
    path('sre-dis',search_district,name='search district'),
    path('pro-fields',project_fields,name='all feild deatails'),
    path("search",search_result, name="search result"),
    path("pro-detail",project_rby_id, name="individual project detail"),
    path('files',pro_files,name='retrive documents'),
    path("modify",modify_project, name="modify with mofification permission"),
    path("delete",project_delete, name='delete project'),
    path('dep-upd',department_update,name='update details for pmu department'),
    path('upd-pro',updated_project_list,name='updated project list'),
    path('upd-id',upd_project_rby_id,name='retrive updated file by name'),
    path('pmu-apl',pmu_approval,name='pmu approval'),
    path('pmu-dec',pmu_decline,name="pmu decline"),
    path('pro-media',media_project_id,name='media details with id'),
    path('upd-media',media_upload,name='\media upload api'),
    path('vid-doc',video_doc_upload,name='adding video and doc'),
    path('dlt-media',media_delete,name='delete media')



]
