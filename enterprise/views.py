from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from django.shortcuts import render
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, RetrieveDestroyAPIView


from .models import Employer, About
from .serializers import  MyVacancySerializer, CompanySerializer
from .permissions import IsOwnerOrReadOnly

# class TransactionsTemplateHTMLRender(TemplateHTMLRenderer):
#     def get_template_context(self, data, renderer_context):
#         data = super().get_template_context(data, renderer_context)
#         if not data:
#             return {}
#         else:
#             return data



class Home(ReadOnlyModelViewSet):
    # renderer_classes = (TemplateHTMLRenderer, )
    # template_name = 'aaaaaaa.html'
    queryset = About.objects.all()
    serializer_class = CompanySerializer

    # def list(self, request, *args, **kwargs):
    #     response = super(Home, self).list(request, *args, **kwargs)
    #     if request.accepted_renderer.format == 'html':
    #         return Response({'data': response.data}, template_name='aaaaaaa.html')
    #     return response


class MyVacancy(ListCreateAPIView):
    #renderer_classes = (TemplateHTMLRenderer, JSONRenderer)
    #template_name = 'video_hosting/home.html'
    #user = self.request.user
    #queryset = Employer.objects.filter(user=user)
    serializer_class = MyVacancySerializer
    permissions_classes = (IsOwnerOrReadOnly, )
    queryset = About.objects.all()
    # def get_queryset(self):
    #     user = self.request.user
    #
    #     my_beats = Q(user=user)
    #
    #     return About.objects.filter(my_beats)

    # def list(self, request, *args, **kwargs):
    #     response = super(MyVacancy, self).list(request, *args, **kwargs)
    #     if request.accepted_renderer.format == 'html':
    #         return Response({'data': response.data}, template_name='video_hosting/home.html')
    #     return response


class PutchVacancy(RetrieveUpdateAPIView):
    queryset = About.objects.all()
    serializer_class = CompanySerializer

class DeleteVacancy(RetrieveDestroyAPIView):
    queryset = About.objects.all()
    serializer_class = MyVacancySerializer