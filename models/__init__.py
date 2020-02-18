"""Packge init file for project package"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
