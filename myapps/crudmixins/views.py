import requests

from django.shortcuts import render, redirect
from rest_framework import generics, mixins

from .models import Student
from .forms import StudentInsertForm
from .serializers import StudentSerializer


class StudentListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


def savestudent(request):
    form = StudentInsertForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)
            post_data = requests.post(
                'http://localhost:8000/api/students/',
                headers={'Content-Type': 'application/json'},
                json=form.cleaned_data
            )
            return redirect('/')
    return render(request, 'core/insert.html', {'form': form})


class StudentRetrieveUpdateDestroy(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = 'student_id'

    def get(self, request, student_id):
        return self.retrieve(request, self.lookup_url_kwarg)

    def put(self, request, student_id):
        return self.update(request, self.lookup_url_kwarg)

    def delete(self, request, student_id):
        return self.destroy(request, self.lookup_url_kwarg)
