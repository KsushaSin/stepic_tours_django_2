from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/index.html', context={

            }
        )


class DepartureView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/departure.html', context={

            }
        )


class TourView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tours/tour.html', context={

            }
        )


def custom_handler404(request, exception):
    return HttpResponseNotFound('Такой страницы не существует!')
