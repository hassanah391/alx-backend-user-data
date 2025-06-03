#!/usr/bin/env python3
"""Module basic_auth"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """Implements basic auth"""
    def extract_base64_authorization_header(
        self,
        authorization_header: str
            ) -> str:
        """returns the Base64 part of the Authorization header
        for a Basic Authentication"""
        if not authorization_header or\
                not isinstance(authorization_header, str) or\
                not authorization_header.startswith('Basic '):
            return None
        return authorization_header[len('Basic '):]

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str
            ) -> str:
        """returns the decoded value of a Base64 string"""
        if (not base64_authorization_header or
                not isinstance(base64_authorization_header, str)):
            return None
        try:
            # Decode from base64 to bytes
            decoded = base64.b64decode(
                base64_authorization_header,
                validate=True
                )
            # Convert bytes to UTF-8 string
            utf8_string = decoded.decode('utf8')
            return utf8_string
        except Exception:
            return None

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
            ) -> Tuple[str, str]:
        """returns the user email and password from
        the Base64 decoded value"""
        if (not decoded_base64_authorization_header or
                not isinstance(decoded_base64_authorization_header, str)
                or ':' not in decoded_base64_authorization_header):
            return (None, None)
        colon_index = decoded_base64_authorization_header.find(':')
        email = decoded_base64_authorization_header[: colon_index]
        password = decoded_base64_authorization_header[colon_index + 1:]
        return (email, password)

    def user_object_from_credentials(
        self,
        user_email: str,
        user_pwd: str
            ) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if (not user_email or not isinstance(user_email, str)
                or not user_pwd) or not isinstance(user_pwd, str):
            return None
        # Search user by email
        try:
            users = User.search({"email": user_email})
        except Exception:
            return None

        if not users:
            return None

        user = users[0]  # Assuming only one user with this email
        if not user.is_valid_password(user_pwd):
            return None

        return user
