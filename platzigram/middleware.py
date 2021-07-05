
from django.shortcuts import redirect
from django.urls import reverse
from users.models import Profile

class ProfileCompletionMiddleware:
    """
    Ensures everyuser has a picture
    """
    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        
        if request.user.is_authenticated:
            if not request.user.is_staff: #lets superusers go to admin page
                profile = request.user.profile
                if not profile.profile_picture or not profile.biography:
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')
        response = self.get_response(request)
        return response