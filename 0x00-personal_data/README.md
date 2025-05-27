# 0x00-personal_data

A Python project focused on handling personal data securely, implementing PII data protection, logging redaction, and password encryption.

## Overview

This project demonstrates best practices for protecting sensitive user information and handling personally identifiable information (PII) in compliance with data privacy standards.

## Features

- **Log Filtering**: Automatically redacts sensitive fields in log messages
- **Password Encryption**: Uses bcrypt for secure password hashing
- **Database Integration**: Connects to MySQL and handles user data securely
- **PII Protection**: Identifies and protects personal identifiable information

## Files

- `filtered_logger.py`: Implements log filtering and redaction of sensitive data
- `encrypt_password.py`: Provides password hashing and validation functionality

## Requirements

- Python 3.7+
- MySQL
- bcrypt package
- mysql-connector-python package

## Usage

### Password Hashing

```python
from encrypt_password import hash_password, is_valid

# Hash a password
hashed = hash_password("MySecurePassword123")

# Verify a password
is_valid(hashed, "MySecurePassword123")  # Returns True
```

### Log Filtering

```python
from filtered_logger import get_logger

logger = get_logger()
logger.info("name=John Doe;email=john@example.com;ssn=123-45-6789;")
# Output will redact sensitive information
```

## Environment Variables

The following environment variables can be set for database connection:

- `PERSONAL_DATA_DB_USERNAME`: Database username (default: "root")
- `PERSONAL_DATA_DB_PASSWORD`: Database password (default: "")
- `PERSONAL_DATA_DB_HOST`: Database host (default: "localhost")
- `PERSONAL_DATA_DB_NAME`: Database name
