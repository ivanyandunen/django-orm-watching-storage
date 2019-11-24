from datacenter.models import Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)

    for visit in visits:
      duration = get_duration(visit.entered_at, timezone.now())
      formatted_duration = format_duration(duration)
      is_strange = is_visit_long(duration)
      non_closed_visits = [
        {
            "who_entered": visit.passcard,
            "entered_at": visit.entered_at,
            "duration": formatted_duration,
            "is_strange": is_strange,
        }
      ]
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
