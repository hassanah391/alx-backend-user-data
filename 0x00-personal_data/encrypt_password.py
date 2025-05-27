#!/usr/bin/env python3
""" Module encrypt_password """
import bcrypt


def hash_password(password: str):
    """returns a salted, hashed password"""
    hased = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hased
