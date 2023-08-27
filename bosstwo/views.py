from django.shortcuts import render
from rest_framework.decorators import api_view
from bosstwo.models import StaffTwo
from django.http import JsonResponse
from rest_framework.response import Response

from bosstwo.serializers import StaffSerializer

# Create your views here.

@api_view(["GET"])
def GetAllStaffs(request):
    try:
        staffs = StaffTwo.objects.all()
        serialized_info = StaffSerializer(staffs, many=True)
        return Response(serialized_info.data)
    except Exception as ex:
        print(ex)
        return Response({"message": ex})
    
@api_view(["GET"])
def GetById(request, staffId):
    try:
        staff = StaffTwo.objects.filter(id=staffId).first()
        serialized_value = StaffSerializer(staff, many=False)
        return Response(serialized_value.data)
    except Exception as ex:
        print(ex)
        return Response({"messsage": ex})
    
@api_view(["GET"])
def GetByStaffId(request, levelId):
    try:
        intLevel = int(levelId)
        stafflevel = StaffTwo.objects.filter(level=intLevel).first()
        serialized_level = StaffSerializer(stafflevel, many=False)
        return Response({"level_result":serialized_level.data})
    except Exception as ex:
        print(ex)
        return Response({"message":ex})


@api_view(["POST"])
def RegisterStaff(request):
    try:
        myinfo = request.data
        Name = myinfo["name"]
        # Age = myinfo["age"]
        Age = int(myinfo["age"])
        Level = myinfo["level"]
        Qualification = myinfo["qualification"]


        stafftwo =StaffTwo(
            name=Name,
            age=Age,
            level=Level,
            qualification=Qualification,
        )
        stafftwo.save()
        register_serialized = StaffSerializer(stafftwo, many=False)
        return Response(register_serialized.data)
    except Exception as ex:
        print(ex)
        return Response({"message": ex})
    

@api_view(["PUT"])
def UpdateStaff(request, id):
    try:
        myinfo = request.data
        name = myinfo["name"]
        age = int(myinfo["age"])
        level = int(myinfo["level"])
        qualification = myinfo["qualification"]

        staff = StaffTwo.objects.filter(id=id).first()
        staff.name = name
        staff.age = age
        staff.level = level
        staff.qualification = qualification

        staff.save()
        edited_serialized_staff = StaffSerializer(staff, many=False)
        return Response(edited_serialized_staff.data)
        # nstaff = StaffTwo.objects.get(id)
    except Exception as ex:
        print(ex)
        return Response({"message": ex})
    
@api_view(["DELETE"])
def DeleteStaff(request, id):
    try:
        delete_staff = StaffTwo.objects.get(pk = id).delete()
        return Response({"message": "staff recorded deleted"})
    except Exception as ex:
        print(ex)
        return Response({"message": ex})

