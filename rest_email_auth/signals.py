"""
Custom signals used by django-rest-email-auth.

These signals allow other applications to easily add custom behavior to
processes from this module.
"""

from django import dispatch


signal = dispatch.Signal()
