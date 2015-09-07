"""
WSGI config for Movie_location project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
#from dj_static import Cling
from django.core.wsgi import get_wsgi_application

#application = Cling(get_wsgi_application())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Movie_location.settings")
application = get_wsgi_application()
