from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime, now


def storage_information_view(request):
    non_closed_visits = []
    time_now = localtime(now())
    visitors = Visit.objects.filter(leaved_at=None)
    for visit in visitors:
        non_closed_visits.append(
            dict(who_entered=visit.passcard.owner_name,
                 entered_at=str(localtime(visit.entered_at)),
                 duration=str(str((time_now - localtime(visit.entered_at))).split('.')[0])))

    context = {'non_closed_visits': non_closed_visits,}
    return render(request, 'storage_information.html', context)
