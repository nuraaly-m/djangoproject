from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class DeveloperLevelMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            experience = int(request.POST.get("experience"))
            if experience < 1:
                return HttpResponseBadRequest("Ваш опыт слишком мал")
            elif experience >= 1 and experience <= 3:
                request.club = "junior"
            elif experience >= 4 and experience <= 6:
                request.club = "middle"
            elif experience >= 7 and experience <= 15:
                request.club = "senior"
            else:
                return HttpResponseBadRequest("Вы слишком опытный")
        elif request.path == "/register/" and request.method == "GET":
            setattr(request, "level", "Уровень не определен")
