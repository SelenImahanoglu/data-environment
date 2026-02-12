# pylint: disable=missing-docstring

"""
This module demonstrates the usage of environment variables.
"""
import os

def start():
    """returns the right message"""
    env = os.getenv("FLASK_ENV")

    if env == "development":
        return "Starting in development mode..."
    if env == "production":
        return "Starting in production mode..."

    return "Starting in empty mode..."
