import os
from pathlib import Path
from dotenv import load_dotenv

# 1. Load the .env file from the root directory
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Basic Security Settings
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-safety-app-key')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['*']

# 3. App Definitions
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'rest_framework',
    'corsheaders',
    # Your local app
    'safety_app',
]

# 4. Middleware (CORS must be at the top)
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'safety_project.urls'
CORS_ALLOW_ALL_ORIGINS = True  # Allows your HTML file to connect

# 5. Database (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 6. Vonage (Nexmo) Credentials from .env
VONAGE_API_KEY = os.getenv('VONAGE_API_KEY', '')
VONAGE_API_SECRET = os.getenv('VONAGE_API_SECRET', '')
VONAGE_FROM_NUMBER = os.getenv('VONAGE_FROM_NUMBER', 'Vonage')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'safety_project.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = '/static/'
