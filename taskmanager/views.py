from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .tasks import auto_complete_task
class TaskList(APIView):
    def get(self, request, id = None):
        try:
 
            data = Task.objects.all().order_by("-id")
            print(data)
  
                 
            dataSer = TaskSerializer(data, many = True)
           
            return Response({
                    "message": "success",
                    "data": dataSer.data,
                    
                }, 200)
        
                
        except Exception as e:
            return Response({
                "message": "Internal Server Error.",
                "error": str(e)
            },500)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class Create(APIView):
    def post(self, request):
        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                task = serializer.save()
                auto_complete_task.apply_async((task.id,), countdown=5*60)  #after 120 second this is automatically completed
                return Response({
                    "message": "success",
                    "data": serializer.data,
                    
                }, 200)
            else:
                return Response({
                "message": "Serialixers errors.",
                "error": serializer.errors
            },400)
        except Exception as e:
            return Response({
                "message": "Internal Server Error.",
                "error": str(e)
            },500)
class deleteTask(APIView):
    def delete(self, request, id=None):
        try:
          
            if id is None:
                return Response({
                    "message": "Enter task Id",
                    "status": 400
                }, 400)
            task = Task.objects.filter(id=id).first()
            if not task:
                return Response({
                    "message": "Not found",
                    "status": 404
                }, 404)
            serializer = TaskSerializer(task, data=request.data, partial= True)
            if serializer.is_valid():
                taskData = serializer.save()
                return Response({
                    "message": "success",
                    "data": serializer.data,
                    "status": 200
                }, 200)
        except Exception as e:
            return Response({
                "message": "Internal Server Error.",
                "error": str(e)
            },500)
class updateTask(APIView):
    def put(self, request, id=None):
        try:
            if id is None:
                return Response({
                    "message": "Enter task Id",
                    "status": 400
                }, 400)
            task = Task.objects.filter(id=id).first()
            if not task:
                return Response({
                    "message": "Not found",
                    "status": 404
                }, 404)
            serializer = TaskSerializer(task, data=request.data, partial = True)
            if serializer.is_valid():
                taskData = serializer.save()
                return Response({
                    "message": "success",
                    "data": serializer.data,
                    "status": 200
                }, 200)
        except Exception as e:
            return Response({
                "message": "Internal Server Error.",
                "error": str(e)
            },500)
            
            
                
            
            
                
                    
  

# Create your views here.
