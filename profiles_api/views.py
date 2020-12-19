from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Use HTTP methiods as functions (get, post, patch, put, delete)',
            'Is similaer to a traditional Django View',
            'Gives you most control over application logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
