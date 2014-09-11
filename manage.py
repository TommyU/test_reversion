#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_revision.settings")

    from django.core.management import execute_from_command_line
    if len(sys.argv)==1:
        sys.argv.extend(['runserver'])
    execute_from_command_line(sys.argv)
