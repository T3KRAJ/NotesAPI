from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import TaskSerializer
from api.models import Task
from rest_framework import generics
from rest_framework import mixins


@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }

    return Response(api_urls)


   #Generic class based views
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'

    def get(self, request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)

    def put(self, request, id, *args, **kwargs):
        return self.update(request, id)

    def delete(self, request, id, *args, **kwargs):
        return self.destroy(request, id)


    #function based views
# @api_view(['GET'])
# def taskList(request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def taskDetail(request, pk):
#     task = Task.objects.get(id=pk)
#     serializer = TaskSerializer(task)
#     return Response(serializer.data)

# @api_view(['POST'])
# def taskCreate(request):
#     serializer = TaskSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])
# def taskUpdate(request, pk):
#     task = Task.objects.get(id=pk)
#     serializer = TaskSerializer( data=request.data, instance=task)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def taskDelete(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()

#     return Response('Item successfully deleted!')
