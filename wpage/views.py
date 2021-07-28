from django.shortcuts import render

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.


class WelcomePageMain(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'wpage/welcome_page.html'

    def get(self, request):
        context = {}
        return Response(context)


class WelcomePageInfo(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'wpage/info.html'

    def get(self, request):
        context = {}
        return Response(context)


class WelcomePageContact(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'wpage/contact.html'

    def get(self, request):
        context = {}
        return Response(context)