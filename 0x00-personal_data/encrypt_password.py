#!/usr/bin/env python3
""" Module encrypt_password """
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password"""
    hased = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hased


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check whether a password is valid or not
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
