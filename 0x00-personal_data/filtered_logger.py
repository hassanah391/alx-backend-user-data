#!/usr/bin/env python3
""" Module filtered_logger """
import logging
from typing import List
import re


def filter_datum(
    fields: List[str], redaction: str,
        message: str, separator: str
        ) -> str:
    """returns the log message obfuscated"""
    return re.sub(
        r'({})=[^{}]*'
        .format('|'.join(map(re.escape, fields)),
                re.escape(separator)),
        lambda m: m.group(1) + '=' + redaction, message
    )
