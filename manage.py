#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

EXPORT_DEPTENCIES = True

def export_dependencies(file_path: str):
    """Export the current dependencies to a requirements.txt file."""
    print(f"Exporting dependencies to {file_path}...")
    os.system(f'pip freeze > {file_path}')


def main():
    if EXPORT_DEPTENCIES:
        export_dependencies('requirements.txt')
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
