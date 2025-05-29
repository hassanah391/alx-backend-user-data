#!/usr/bin/env python3
""" Module auth """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class for authentication system"""
    def require_auth(
        self, path: str,
        excluded_paths: List[str]
    ) -> bool:
        """Checks If an endpoint requires auth"""
        if path is None or\
            excluded_paths is None or\
                len(excluded_paths) == 0:
            return True
        # make sure that a path end with a slash
        # to make require_auth() slash tolerant
        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ Validate all requests to secure the API """
        if request is None:
            return None
        # validate that the request have Authorization key
        authorization = request.headers.get('Authorization')
        if authorization is None:
            return None

        return authorization

    def current_user(self, request=None) -> TypeVar('User'):
        """do know yet"""
        return None
