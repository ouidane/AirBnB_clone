#!/usr/bin/python3
"""magic method for models directory."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
