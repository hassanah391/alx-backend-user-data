#!/usr/bin/env python3
""" Module filtered_logger """
import logging
from typing import List
import re
import os
import mysql.connector
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
    """
    Returns a connector to the database using credentials from environment variables.
    
    Environment variables:
    - PERSONAL_DATA_DB_USERNAME: Database username (default: "root")
    - PERSONAL_DATA_DB_PASSWORD: Database password (default: "")
    - PERSONAL_DATA_DB_HOST: Database host (default: "localhost")
    - PERSONAL_DATA_DB_NAME: Database name (required)
    
    Returns:
        MySQLConnection: A connection object to the MySQL database
    """
    # Get database credentials from environment variables with defaults
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')
    
    # Create and return the database connection
    connection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )
    
    return connection
