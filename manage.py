#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'explorateur_ia.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Django n'est pas installé.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()