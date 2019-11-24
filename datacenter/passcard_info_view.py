from datacenter.models import Passcard
from datacenter.models import Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    
    this_passcard_visits = []

    for visit in visits:
      duration = get_duration(visit.entered_at, visit.leaved_at)
      formatted_duration = format_duration(duration)
      is_strange = is_visit_long(duration)
      this_passcard_visits.append(
          {
              "entered_at": visit.entered_at,
              "duration": formatted_duration,
              "is_strange": is_strange
          },
      )
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
