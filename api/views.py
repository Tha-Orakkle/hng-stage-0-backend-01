from django.utils.timezone import datetime
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class UserDetails(APIView):
    """
    UserDetails API view to handle GET requests.

    Methods:
        get(request): Returns user details including email, current datetime, and GitHub link.

    """

    def get(self, request):
        """
        Handles GET requests and returns user details including email, current datetime, and GitHub link.
        """
        data = {
            'email': 'adegbiranayinoluwa.paul@yahoo.com',
            'current_datetime': datetime.now().isoformat() + 'Z',
            'github_link': '<https://github.com/Tha-Orakkle/hng-stage-0-backend-01.git>',
        }
        return Response(data, status=200)
