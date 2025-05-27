#!/usr/bin/env python3
""" Module filtered_logger """
import logging
from typing import List
import re
import os
import mysql.connector 
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.connection import MySQLConnection


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Takes record message and obfuscate it using filter_datum()
            then log the obfuscated mesage with a specific format
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR
            )
        return super().format(record)


def get_logger() -> logging.Logger:
    """Create and return a logger with StreamHandler and RedactingFormatter"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create StreamHandler with RedactingFormatter
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))

    # Add the handler to the logger
    logger.addHandler(stream_handler)

    return logger


def get_db() -> MySQLConnection:
    """Returns a connector to the database"""
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME', 'my_db')

    connector = mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=db_name
    )
    return connector
