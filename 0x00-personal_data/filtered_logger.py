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
    for field in fields:
        match = re.search("{}=([^{}]+)".format(field, separator), message)
        if match:
            message = re.sub("{}".format(match.group(1)), redaction, message)
    return message
