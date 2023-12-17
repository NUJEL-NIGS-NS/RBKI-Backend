from django.shortcuts import render
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
import csv
import datetime
from rest_framework.response import Response
from .serializer import (
    ProjectSerializer,
    ProjectDisplaySerializer,
    UpdateProjectSerializer,
    UpdateDisplaySerializer,
)
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.db.models import Sum, Count

fs = FileSystemStorage(location="/temp")
# Create your views here.


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def bulk_update_db(request):
    data = {}
    if request.user.department == "PMU":
        try:
            file = request.FILES["file"]
            content = file.read()
            file_content = ContentFile(content)
            file_name = fs.save(file.name, file_content)
            tmp_file = fs.path(file_name)
            csv_file = open(tmp_file, errors="ignore")
            reader = csv.reader(csv_file)
            next(reader)

            project_list = []
            for row in reader:
                (
                    pro_name,
                    district,
                    lac,
                    local_bdy,
                    stage,
                    as_no,
                    as_date,
                    as_amt,
                    ts_no,
                    ts_date,
                    ts_amt,
                    reas_no,
                    reas_date,
                    reas_amt,
                    s_date,
                    pro_cat,
                    length_m,
                    lat_tude,
                    log_tude,
                    status,
                    piu,
                    c_name,
                    c_phone,
                    c_email,
                    c_pan,
                    tender_no,
                    tender_data,
                    tender_amt,
                    agr_no,
                    agr_date,
                    arg_amt,
                    hand_to_date,
                    period,
                    completion_date,
                    utility,
                    mait_charge,
                    total_exp,
                    fin_pro,
                    phy_pro,
                    updated_by,
                ) = row
                as_date = datetime.datetime.strptime(as_date, "%d-%m-%Y")
                ts_date = datetime.datetime.strptime(ts_date, "%d-%m-%Y")
                reas_date = datetime.datetime.strptime(reas_date, "%d-%m-%Y")
                s_date = datetime.datetime.strptime(s_date, "%d-%m-%Y")
                tender_data = datetime.datetime.strptime(tender_data, "%d-%m-%Y")
                agr_date = datetime.datetime.strptime(agr_date, "%d-%m-%Y")
                hand_to_date = datetime.datetime.strptime(hand_to_date, "%d-%m-%Y")
                completion_date = datetime.datetime.strptime(
                    completion_date, "%d-%m-%Y"
                )
                project_list.append(
                    Project(
                        pro_name=pro_name,
                        district=district,
                        lac=lac,
                        local_bdy=local_bdy,
                        stage=stage,
                        as_no=as_no,
                        as_date=as_date.date(),
                        as_amt=as_amt,
                        ts_no=ts_no,
                        ts_date=ts_date.date(),
                        ts_amt=ts_amt,
                        reas_no=reas_no,
                        reas_date=reas_date.date(),
                        reas_amt=reas_amt,
                        s_date=s_date.date(),
                        pro_cat=pro_cat,
                        length_km=length_m,
                        lat_tude=lat_tude,
                        log_tude=log_tude,
                        status=status,
                        piu=piu,
                        c_name=c_name,
                        c_phone=c_phone,
                        c_email=c_email,
                        c_pan=c_pan,
                        tender_no=tender_no,
                        tender_data=tender_data.date(),
                        tender_amt=tender_amt,
                        agr_no=agr_no,
                        agr_date=agr_date.date(),
                        arg_amt=arg_amt,
                        hand_to_date=hand_to_date.date(),
                        period=period,
                        completion_date=completion_date.date(),
                        utility=utility,
                        mait_charge=mait_charge,
                        total_exp=total_exp,
                        fin_pro=fin_pro,
                        phy_pro=phy_pro,
                        updated_by=updated_by,
                    )
                )
            Project.objects.bulk_create(project_list)
            data["status"] = "sucessfully uploaded"
        except Exception as e:
            print(e)
            data["status"] = "uploading Failed"
    else:
        data["status"] = "You are not Authorized to upload files to DataBase"
    return Response(data)


# --------------------------------------------------------------------------------------------------------------------------
# view for adding a project


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_project(request):
    data = {}
    try:
        new_project = ProjectSerializer(data=request.data)
        if new_project.is_valid():
            new_project.save()
            data["status"] = "project added"
        else:
            data["status"] = "process faled"

    except Exception as e:
        data["status"] = "process failed " + str(e)
    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
# All project pagination


class Project_page(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDisplaySerializer
    pagination_class = PageNumberPagination
    authentication_classes = [TokenAuthentication]  # Add Token Authentication
    permission_classes = [IsAuthenticated]


# ------------------__________________________________-------------------------_____________________------------
# dashboard data


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def Project_dashdata(request):
    data = {}
    try:
        as_awarded = Project_constants.objects.filter(as_id=1).values("as_awarded")[0][
            "as_awarded"
        ]
        all_RKI = Project_constants.objects.filter(as_id=1).values("alc_fr_rki")[0][
            "alc_fr_rki"
        ]
        as_total = Project.objects.aggregate(total=Sum("as_amt"))["total"]
        as_count = Project.objects.aggregate(count=Count("as_no"))["count"]
        wrk_cpl = Project.objects.filter(stage="Completed").aggregate(
            count=Count("as_no")
        )["count"]

        pro_lngt = Project.objects.aggregate(total=Sum("length_km"))["total"]
        cmp_lngt = Project.objects.filter(stage="Completed").aggregate(
            total=Sum("length_km")
        )["total"]
        district = Project.objects.values("district").annotate(total=Count("district"))
        status = Project.objects.values("stage").annotate(total=Count("id"))
        wrk_exp = Project.objects.aggregate(total=Sum("total_exp"))["total"]
        pro_cat = Project.objects.values("pro_cat").annotate(total=Count("id"))

        data["as_awarded"] = as_awarded
        data["all_RKI"] = all_RKI
        data["as_total"] = as_total
        data["count"] = as_count
        data["workCmp"] = wrk_cpl
        data["length_pro"] = pro_lngt
        data["length_cmp"] = cmp_lngt
        data["wrk_exp"] = wrk_exp
        data["status"] = status
        data["district_wise"] = district
        data["procat"] = pro_cat

        pass
    except Exception as e:
        print(e)
    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  district search
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def search_district(request):
    data = {}
    try:
        field = request.GET.get("field")

        result_list = Project.objects.values_list(field).distinct()

        data["result_list"] = result_list

    except Exception as e:
        data["Error"] = e
    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  list of fields


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def project_fields(request):
    data = {
        "Project Name": "pro_name",
        "District": "district",
        "Legistative assembly council": "lac",
        "Local Body": "local_bdy",
        "completed/under construction": "stage",
        "administrative sanction no": "as_no",
        "administrative sanction date": "as_date",
        "administrative sanction amount": "as_amt",
        "technical sanction no]": "ts_no",
        "technical sanction date": "ts_date",
        "technical sanction amount": "ts_amt",
        "revised administrative sanction no": "reas_no",
        "revised administrative sanction Date": "reas_date",
        "revised administrative sanction Amount": "reas_amt",
        "Starting Date": "s_date",
        "Project Category": "pro_cat",
        "length": "length_km",
        "lattitude": "lat_tude",
        "logitude": "log_tude",
        "current progress": "status",
        "PIU": "piu",
        "contractor Name": "c_name",
        "contractor phone": "c_phone",
        "contractor email": "c_email",
        "contractor_PAN": "c_pan",
        "Tender Number": "tender_no",
        "Tender Date": "tender_data",
        "Tender Amount": "tender_amt",
        "agreement no": "agr_no",
        "agreement date": "agr_date",
        "agreement amount": "arg_amt",
        "handover date": "hand_to_date",
        "period of completion": "period",
        "Complition Date": "completion_date",
        "utility shifting&its amount": "utility",
        "maintenance charge": "mait_charge",
        "Total Expenditure": "total_exp",
        "financial Progress": "fin_pro",
        "Physical Progress": "phy_pro",
        "Updated By": "updated_by",
        "Last Update": "last_upd",
    }
    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  Search result


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def search_result(request):
    data = {}
    try:
        field = request.GET.get("field")
        search = request.GET.get("search")
        result = Project.objects.filter(**{f"{field}__icontains": search})
        result_sr = ProjectDisplaySerializer(result, many=True)
        data["results"] = result_sr.data
    except Exception as e:
        data["error"] = str(e)  # You can provide an error message here

    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  Project Details by id
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def project_rby_id(request):
    data = {}
    try:
        id_ = request.GET.get("id")
        pro_data = Project.objects.get(
            id=id_
        )  # Use .get() to retrieve a single instance
        sre_data = ProjectSerializer(pro_data)  # Serialize the single instance
        data["result"] = sre_data.data  # Access the serialized data using .data
    except Project.DoesNotExist:
        data[
            "error"
        ] = "Project not found"  # Handle the case where the project doesn't exist
    except Exception as e:
        data["error"] = str(e)

    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  Project file
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def pro_files(request):
    data = {}
    try:
        p_name = request.GET.get("name", None)
        if p_name != None:
            file = Project_file.objects.filter(pro_name=p_name).values_list("doc")
            data["result"] = file
        else:
            data["result"] = "No files"
    except Exception as e:
        data["error"] = str(e)

    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  Projectmodify


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def modify_project(request):
    data = {}
    form = request.data
    id = request.GET.get("id", None)
    try:
        if request.user.department == "PMU":
            if id:
                instance = Project.objects.get(id=id)
                row = ProjectSerializer(instance=instance, data=form)
                if row.is_valid():
                    up_data = row.save()
                    data["status"] = "Successfully Updated"
                else:
                    data["status"] = "Error in Data Inserted"
                    data["error"] = row.errors

            else:
                row = ProjectSerializer(data=form)
                if row.is_valid():
                    up_data = row.save()
                    data["status"] = "Successfully Updated"
                else:
                    data["status"] = "Error in Data Inserted"
                    data["error"] = row.errors

        else:
            if id:
                try:
                    check_upd = Update_cache_table.objects.get(pro_id=id)
                    instance = Update_project.objects.get(id=check_upd.upd_id)
                    row = UpdateProjectSerializer(instance=instance, data=form)
                    if row.is_valid():
                        up_data = row.save()
                        data["status"] = "Successfully Updated And Waiting for Approval"
                    else:
                        data["status"] = "Error in Data Inserted"
                        data["error"] = row.errors

                except:
                    row = UpdateProjectSerializer(data=form)
                    if row.is_valid():
                        up_data = row.save()
                        upd_cache = Update_cache_table(pro_id=id, upd_id=up_data.id)
                        upd_cache.save()
                        data["status"] = "Successfully Updated And Waiting for Approval"
                    else:
                        data["status"] = "Error in Data Inserted"
                        data["error"] = row.errors

            else:
                row = UpdateProjectSerializer(data=form)
                if row.is_valid():
                    up_data = row.save()
                    # upd_cache = Update_cache_table(pro_id=id, upd_id=up_data.id)
                    # upd_cache.save()
                    data["status"] = "Successfully Updated And Waiting for Approval"
                else:
                    data["status"] = "Error in Data Inserted"
                    data["error"] = row.errors

    except Exception as e:
        print(e)

    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  Project  Delete


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def project_delete(request):
    data = {}
    id = request.GET.get("id", None)
    try:
        if request.user.department == "PMU":
            obj = Project.objects.get(id=id)
            obj.delete()
            data["status"] = "sucessfully deleted"
        else:
            data["status"] = "You are not Authorised to delete this data"

    except Exception as e:
        data["Error"] = str(e)
    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  Departmental details


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def department_update(request):
    data = {}
    obj = Update_project.objects.count()
    data["count"] = obj
    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  upadte details
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updated_project_list(request):
    data = {}
    try:
        obj = Update_project.objects.all()
        serialize = UpdateDisplaySerializer(obj, many=True)
        data["projects"] = serialize.data
    except Exception as e:
        data["error"] = str(e)

    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  individual update details


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def upd_project_rby_id(request):
    data = {}
    try:
        id_ = request.GET.get("id")
        pro_data = Update_project.objects.get(id=id_)
        sre_data = UpdateProjectSerializer(pro_data)
        data["result"] = sre_data.data
    except Update_project.DoesNotExist:  # Use the correct exception class
        data[
            "error"
        ] = "Project not found"  # Handle the case where the project doesn't exist
    except Exception as e:
        data["error"] = str(e)

    try:
        upd_cache = Update_cache_table.objects.get(upd_id=id_)
        data["type"] = "Updated"
        data["id"] = upd_cache.pro_id  # Access the id from the retrieved object
    except Update_cache_table.DoesNotExist:  # Use the correct exception class
        data["type"] = "New Project"
    except Exception as e:
        data["error"] = str(e)

    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  approving pmu


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def pmu_approval(request):
    data = {}
    form = request.data
    id = request.GET.get("id", None)

    try:
        obj = Update_cache_table.objects.get(upd_id=id)
        upd_obj = Project.objects.get(id=obj.pro_id)

        # Try to update the existing project
        row = ProjectSerializer(instance=upd_obj, data=form)
        if row.is_valid():
            up_data = row.save()
            obj_up_tab = Update_project.objects.get(id=obj.upd_id)
            obj.delete()
            obj_up_tab.delete()
            data["status"] = "Successfully Updated"
        else:
            data["status"] = "Error in Data Inserted"
            data["error"] = row.errors

    except Update_cache_table.DoesNotExist:
        # If the update does not exist, create a new project
        row = ProjectSerializer(data=form)
        if row.is_valid():
            up_data = row.save()
            print("hi")
            obj_up_tab = Update_project.objects.get(id=id)
            obj_up_tab.delete()
            data["status"] = "Successfully Inserted"
        else:
            data["status"] = "Error in Data Inserted"
            data["error"] = row.errors

    except Exception as e:
        data["error"] = str(e)

    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  decline Pmu
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def pmu_decline(request):
    data = {}
    id = request.GET.get("id", None)

    try:
        # Attempt to get the Update_cache_table object
        uct = Update_cache_table.objects.get(upd_id=id)
        uct.delete()

        # Delete the corresponding Update_project object
        UP_obj = Update_project.objects.get(id=id)
        UP_obj.delete()

        data["status"] = "Successfully Declined and Deleted"
    except Update_cache_table.DoesNotExist:
        # If Update_cache_table does not exist, try to delete only Update_project
        try:
            UP_obj = Update_project.objects.get(id=id)
            UP_obj.delete()
            data["status"] = "Successfully Declined and Deleted"
        except Update_project.DoesNotExist:
            data["status"] = "Update_project does not exist"
    except Exception as e:
        data["error"] = str(e)

    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  meda wih id


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def media_project_id(request):
    data = {}
    id = request.GET.get("id", None)
    try:
        result = Project_image.objects.filter(pro_name_id=id).values_list("image")
        if len(result) == 0:
            data["image"] = 0
        else:
            data["image"] = result
    except Project_image.DoesNotExist:
        data["image"] = 0

    try:
        result = Project_file.objects.filter(pro_name_id=id).values_list("doc")
        if len(result) == 0:
            data["file"] = 0
        else:
            data["file"] = result
    except Project_file.DoesNotExist:
        data["file"] = 0

    try:
        result = Project_Video.objects.filter(pro_name_id=id).values_list("video")
        if len(result) == 0:
            data["Video"] = 0
        else:
            data["Video"] = result
    except Project_Video.DoesNotExist:
        data["Video"] = 0

    except Exception as e:
        data["error"] = str(e)

    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  meda to database (image)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def media_upload(request):
    data = {}
    id = request.GET.get("id", None)
    uploaded_files = request.FILES.getlist("image")

    try:
        for index, file in enumerate(uploaded_files):
            project_image = Project_image(pro_name_id=id, image=file)
            project_image.save()

        data["status"] = "Upload successful"
    except Exception as e:
        data["error"] = str(e)
    return Response(data)


# ------------------__________________________________-------------------------_____________________------------
#  meda to database (image)
@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def video_doc_upload(request):
    data = {}
    id = request.GET.get("id", None)
    type = request.GET.get("type", None)
    try:
        if type == "video":
            uploaded_files = request.FILES.getlist("video")
            for i in uploaded_files:
                pro_video = Project_Video(pro_name_id=id, video=i)
                pro_video.save()
                data["status"] = "Upload successful"
        elif type == "Doc":
            uploaded_files = request.FILES.getlist("Doc")
            for i in uploaded_files:
                pro_video = Project_file(pro_name_id=id, doc=i)
                pro_video.save()
                data["status"] = "Upload successful"
        else:
            data["status"] = "type error"

    except Exception as e:
        data["status"] = str(e)
    return Response(data)

# ------------------__________________________________-------------------------_____________________------------
#   Media delete (all)
@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def media_delete(request):
    data = {}
    id = request.GET.get("id", None)
    type = request.GET.get("type", None)
    try:
        if type == 'image':
            objs = Project_image.objects.filter(pro_name_id=id)
            for obj in objs:
                obj.image.delete()  # Delete associated file
                obj.delete()        # Delete model instance

            data['status'] = 'deleted Sucessfully'
        elif type == 'video':
            objs = Project_Video.objects.filter(pro_name_id=id)
            for obj in objs:
                obj.video.delete()  # Delete associated file
                obj.delete() 
            data['status'] = 'deleted Sucessfully'  
        elif type == 'doc':
            objs= Project_file.objects.filter(pro_name_id=id)  
            for obj in objs:
                obj.doc.delete()  # Delete associated file
                obj.delete()
            data['status'] = 'deleted Sucessfully'     
        else:
            data["status"] = "type error"
    except Exception as e:
        data['error'] = str(e)
    return Response(data)
            
