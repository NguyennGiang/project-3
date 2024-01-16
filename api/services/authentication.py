from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed, ParseError

User = get_user_model()


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        jwt_token = request.headers.get('Authorization')
        if not jwt_token:
            return None
        jwt_token = JWTAuthentication.get_the_token_from_header(jwt_token)
        try:
            payload = jwt.decode(jwt_token, settings.JWT_CONF['ACCESS_TOKEN_SECRET_KEY'], algorithms=['HS256'])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed('Invalid signature')
        except ParseError:
            raise ParseError()

            # Get the user from the database
        user_id = payload.get('user')
        if user_id is None:
            raise AuthenticationFailed('User identifier not found in JWT')

        user = User.objects.filter(id=user_id).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        request.user = user
        # Return the user and token payload
        return user, payload

    @classmethod
    def create_jwt(cls, user) -> dict:
        # Create the JWT payload
        access_token_payload = {
            'exp': int((datetime.now() + settings.JWT_CONF['ACCESS_TOKEN_LIFETIME']).timestamp()),
            # set the expiration time for 5 hour from now
            'iat': datetime.now().timestamp(),
            'user': str(user.id)
        }

        access_token = jwt.encode(access_token_payload, settings.JWT_CONF['ACCESS_TOKEN_SECRET_KEY'], algorithm='HS256')

        refresh_token_payload = {
            'exp': int((datetime.now() + settings.JWT_CONF['REFRESH_TOKEN_LIFETIME']).timestamp()),
            # set the expiration time for 5 hour from now
            'iat': datetime.now().timestamp(),
            'user': str(user.id)
        }

        refresh_token = jwt.encode(access_token_payload, settings.JWT_CONF['REFRESH_TOKEN_SECRET_KEY'], algorithm='HS256')

        return dict(token=access_token, refresh_token=refresh_token)

    def authenticate_header(self, request):
        return 'JWT'

    @classmethod
    def get_the_token_from_header(cls, jwt_token):
        token = jwt_token.replace("JWT", "").strip()
        return token
