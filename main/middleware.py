from django.utils import timezone
from django.contrib.auth import get_user

from .models import PageVisit

class TrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user = get_user(request)
        if user.is_authenticated:
            page_visit, created = PageVisit.objects.get_or_create(
                user=user,
                path=request.path,
            )

            # Get user's IP address
            ip_address = request.META.get('REMOTE_ADDR')

            # Calculate time spent on page
            if page_visit.start_time is not None:
                time_spent = (timezone.now() - page_visit.start_time).total_seconds()
                page_visit.time_spent += time_spent # type: ignore
                page_visit.save()
                
                # Convert time spent to minutes and save to the model
                minutes_spent = int(time_spent // 60)
                page_visit.time_spent_minutes = minutes_spent
                page_visit.save()


            # Update visit count, last visit time, and IP address
            page_visit.visit_count += 1
            page_visit.last_visit = timezone.now()
            page_visit.start_time = timezone.now()
            page_visit.ip_address = ip_address
            page_visit.save()

        return response
