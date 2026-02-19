import os
from django.core.wsgi import get_wsgi_application

# Use 'settings' if settings.py is in the same folder, 
# or 'safety_project.settings' if it's nested.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'safety_project.settings')

application = get_wsgi_application()
