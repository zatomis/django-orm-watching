from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime , now


def normal_time(time_in,time_out):
    if (time_out):
        return str(str(time_out-time_in).split('.')[0])
    else:
        return 'in the vault'

def is_visit_long(visit, minutes = 15):
    if not (visit.leaved_at):
        return False
    if (visit.leaved_at.timestamp()-visit.entered_at.timestamp()) > minutes * 60:
        return True
    else:
        return False

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.first()
    this_passcard_visits = []
    time_now = localtime(now())
    passcard_visit = Visit.objects.filter(passcard=passcard)
    for visit in passcard_visit:
        this_passcard_visits.append(
            dict(entered_at=visit.entered_at,
                 duration=normal_time(localtime(visit.entered_at), localtime(visit.leaved_at)),
                 is_strange=is_visit_long(visit, 1000)))
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
