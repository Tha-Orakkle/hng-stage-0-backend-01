from django.utils.timezone import datetime
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class LandingPage(APIView):
    """
    LandingPage API view to handle GET requests.

    Methods:
        get(request): Returns a welcome message.

    """

    def get(self, request):
        """
        Handles GET requests and returns a welcome message.
        """
        return Response({
            'message': 'Welcome to the HNG Stage 0 Backend Task 1 API',
            'author': 'tha_orakkle',
            'endpoints': {
                'user-details': '/api/user/',
            }
        }, status=200)
    

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
            'github_link': 'https://github.com/Tha-Orakkle/hng-stage-0-backend-01',
        }
        return Response(data, status=200)
