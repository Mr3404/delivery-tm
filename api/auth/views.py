from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import ParseError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password




class Register(APIView):

    def post(self, request):
        try:
            user = User.objects.create(
                username = request.data["username"],
                password = make_password(request.data["password"])
            )
            # add verification function later here
            serializer = RefreshToken.for_user(user)
            return Response({"token":str(serializer.access_token)})
        except Exception as e:
            raise ParseError(e)