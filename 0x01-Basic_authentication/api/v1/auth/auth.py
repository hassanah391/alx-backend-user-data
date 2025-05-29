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
        """Checks If an endpoint require auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """ do know yet """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """do know yet"""
        return None
