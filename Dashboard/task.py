from .models import tasks
from django.db import transaction
from django.utils import timezone
def update_date():
    revision_freq={0: 2, 1: 4, 2: 7, 3: 15, 4: 30}                  ## if total revision = key(here) then add next revision after value(here) no. of days
    fine_freq = {1: 2, 2: 4, 3: 10, 4: 15, 5: 30}                   ## if total revision = key(here) and if pending from value(here) days then  decrease 1 revision count
    try:
        obj_to_update_marked = tasks.objects.filter(marked=True)
        with transaction.atomic():
            for obj in obj_to_update_marked:
                obj.TotalRevision +=1
                if obj.TotalRevision>=5:
                    days_to_add = 60
                else:
                    days = fine_freq[obj.TotalRevision]
                    if timezone.now().date() - obj.RevisionDate > timezone.timedelta(days=days):
                        obj.TotalRevision -= 1
                    days_to_add = revision_freq[obj.TotalRevision]
                obj.RevisionDate = timezone.now().date()+timezone.timedelta(days=days_to_add)
                obj.marked=False
                obj.save()
                print(obj.TotalRevision,obj.RevisionDate,'Revision of marked')
    except Exception as e:
        print(e.__str__())
