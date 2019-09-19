"""
Django settings for vmi (Verify My Identity) project.
Copyright Videntity Systems Inc.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import dj_database_url
from django.contrib.messages import constants as messages
from getenv import env
from .utils import bool_env
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@+ttixefm9-bu1eknb4k^5dj(f1z0^97b$zan9akdr^4s8cc54'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool_env(env('DEBUG', True))

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
    'social_django',
    'phonenumber_field',
    'oauth2_provider',
    'rest_framework',
    'django_filters',
    'apps.oidc',
    'apps.home',
    'apps.accounts',
    'apps.ial',
    'apps.fido',
    'apps.mfa.backends.sms',
    'apps.api',
    # 'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'apps.mfa.middleware.DeviceVerificationMiddleware',
    'apps.mfa.middleware.AssertDeviceVerificationMiddleware',
    'apps.oidc.error_handlers.AuthenticationRequiredExceptionMiddleware',
    'apps.oidc.error_handlers.OIDCNoPromptMiddleware',
]


AUTHENTICATION_BACKENDS = (
    'social_core.backends.google_openidconnect.GoogleOpenIdConnect',
    'django.contrib.auth.backends.ModelBackend',

)


SOCIAL_AUTH_GOOGLE_URL = env(
    "SOCIAL_AUTH_GOOGLE_URL", 'https://accounts.google.com')
SOCIAL_AUTH_GOOGLE_OIDC_ENDPOINT = env(
    "SOCIAL_AUTH_GOOGLE_OIDC_ENDPOINT", 'https://accounts.google.com')

SOCIAL_AUTH_GOOGLE_OPENIDCONNECT_KEY = env(
    'SOCIAL_AUTH_GOOGLE_OPENIDCONNECT_KEY', '')
SOCIAL_AUTH_GOOGLE_OPENIDCONNECT_SECRET = env(
    'SOCIAL_AUTH_GOOGLE_OPENIDCONNECT_SECRET', '')
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'


VERIFICATION_BACKENDS = [
    'apps.fido.auth.backends.FIDO2Backend',
    'apps.mfa.backends.sms.backend.SMSBackend',
]

SMS_CODE_CHARSET = "1234567890"

ROOT_URLCONF = 'vmi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
            ],
        },
    },
]


WSGI_APPLICATION = 'vmi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASES_CUSTOM',
                    'sqlite:///{}/db.sqlite3'.format(BASE_DIR))),
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AWS_STORAGE_BUCKET_NAME = env(
    "AWS_STORAGE_BUCKET_NAME", "development-vmi-media-storage")
AWS_AUTO_CREATE_BUCKET = True
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False
DEFAULT_FILE_STORAGE = env("DEFAULT_FILE_STORAGE",
                           'django.core.files.storage.FileSystemStorage')
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
# MEDIA_URL = 'http://localhost:8000/media/'
MEDIA_URL = '/media/'

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'sitestatic'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static-assets"),
]

ATOMIC_REQUESTS = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

# OAUTH SETTINGS
OAUTH2_PROVIDER = {
    'SCOPES': {'openid': 'open id connect access'},
    'DEFAULT_SCOPES': ['openid'],

    'OAUTH2_VALIDATOR_CLASS': 'vmi.oauth2_validators.SingleAccessTokenValidator',
    'OAUTH2_SERVER_CLASS': 'apps.oidc.server.Server',
    'REQUEST_APPROVAL_PROMPT': 'auto',
    'ACCESS_TOKEN_EXPIRE_SECONDS':  int(env('ACCESS_TOKEN_EXPIRE_SECONDS', 315360000))
}
OAUTH2_PROVIDER_GRANT_MODEL = 'oidc.Grant'
OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL = 'oauth2_provider.AccessToken'
OAUTH2_PROVIDER_APPLICATION_MODEL = 'oauth2_provider.Application'

OAUTH2_PROVIDER_REFRESH_TOKEN_MODEL = 'oauth2_provider.RefreshToken'
OAUTH2_PROVIDER_ALLOWED_GRANT_TYPES = (
    "authorization_code",
    # "password",
    # "client_credentials",
    "refresh_token",
)
OAUTH2_PROVIDER_ALLOWED_RESPONSE_TYPES = (
    # "token",
    "code",
)
OIDC_PROVIDER = {
    # 'OIDC_ISSUER': 'http://localhost:8000',
    'OIDC_BASE_CLAIM_PROVIDER_CLASS': 'apps.oidc.claims.ClaimProvider',
    'OIDC_CLAIM_PROVIDERS': [
        # Mandatory
        'apps.oidc.claims.UserClaimProvider',

        # Optional
        # The USerProfileClaimProvider currently gets all claims fetch-able via the
        # UserProfile.
        'apps.accounts.claims.UserProfileClaimProvider',
        'apps.accounts.claims.AddressClaimProvider',
        'apps.accounts.claims.IdentifierClaimProvider',
        'apps.accounts.claims.OrganizationAgentClaimProvider',
        'apps.accounts.claims.MembershipClaimProvider',
        'apps.accounts.claims.VerifiedPersonDataClaimProvider',
        # 'apps.accounts.claims.SubjectClaimProvider',
        # 'apps.accounts.claims.EmailVerifiedClaimProvider',
        # 'apps.accounts.claims.PhoneNumberClaimProvider',
        # 'apps.accounts.claims.IdentityAssuranceLevelClaimProvider',
        # 'apps.accounts.claims.AuthenticatorAssuranceLevelClaimProvider',
        # 'apps.accounts.claims.VectorsOfTrustClaimProvider',
        'apps.fido.claims.AuthenticatorAssuranceProvider',
        'apps.mfa.backends.sms.claims.AuthenticatorAssuranceProvider',
    ],
}


# Add a prefix to the lugh checkdigit calculation.
# This can help identify genuine subject ids and indicate provenance.
SUBJECT_LUHN_PREFIX = env('SUBJECT_LUHN_PREFIX', '')
APPLICATION_TITLE = env('DJANGO_APPLICATION_TITLE', "Share My Health Accounts")
KILLER_APP_TITLE = env('KILLER_APP_TITLE', 'Share My Health')
KILLER_APP_URI = env('KILLER_APP_URI', 'https://app.sharemy.health')

TOP_LEFT_TITLE = env('TOP_LEFT_TITLE', 'Verify My Identity')

ORGANIZATION_TITLE = env(
    'DJANGO_ORGANIZATION_TITLE',
    'Alliance for Better Health')
ORGANIZATION_URI = env('DJANGO_ORGANIZATION_URI', 'https://abhealth.us')
POLICY_URI = env(
    'DJANGO_POLICY_URI',
    'http://sharemy.health/privacy-policy1.0.html')
POLICY_TITLE = env('DJANGO_POLICY_TITLE', 'Privacy Policy')
TOS_URI = env('DJANGO_TOS_URI',
              'http://sharemy.health/terms-of-service1.0.html')
TRAINING_URI = env('DJANGO_TRAINING_URI',
                   'http://sharemy.health/training1.0.html')
TOS_TITLE = env('DJANGO_TOS_TITLE', 'Terms of Service')
EXPLAINATION_LINE = ('This is an instance of Verify My Identity, \
                     an open source OpenID Connect Identity Provider.')
EXPLAINATION_LINE = env('DJANGO_EXPLAINATION_LINE ', EXPLAINATION_LINE)
USER_DOCS_URI = "https://abhealth.us"
USER_DOCS_TITLE = "User Documentation"
USER_DOCS = "User Docs"
# LINKS TO DOCS
DEVELOPER_DOCS_URI = "https:/abhealth.us"
DEVELOPER_DOCS_TITLE = "Developer Documentation"
DEVELOPER_DOCS = "Developer Docs"
DEFAULT_DISCLOSURE_TEXT = """
    Unauthorized or improper use of this
    system or its data may result in disciplinary action, as well as civil
    and criminal penalties. This system may be monitored, recorded and is
    subject to audit.
    """

DISCLOSURE_TEXT = env('DJANGO_PRIVACY_POLICY_URI', DEFAULT_DISCLOSURE_TEXT)

HOSTNAME_URL = env('HOSTNAME_URL', 'http://localhost:8000')

ORG_SIGNUP_CONTACT = env('ORG_SIGNUP_CONTACT',
                         'https://abhealth.us/contact-us/')

# Allow Members to create accounts
ALLOW_MEMBER_SIGNUP = bool_env(env('ALLOW_MEMBER_SIGNUP', False))

SETTINGS_EXPORT = [
    'DEBUG',
    'ALLOWED_HOSTS',
    'APPLICATION_TITLE',
    'STATIC_URL',
    'STATIC_ROOT',
    'DEVELOPER_DOCS_URI',
    'DEVELOPER_DOCS_TITLE',
    'ORGANIZATION_TITLE',
    'POLICY_URI',
    'POLICY_TITLE',
    'DISCLOSURE_TEXT',
    'TOS_URI',
    'TOS_TITLE',
    'EXPLAINATION_LINE',
    'USER_DOCS_URI',
    'USER_DOCS',
    'DEVELOPER_DOCS',
    'USER_DOCS_TITLE',
    'HOSTNAME_URL',
    'TOP_LEFT_TITLE',
    'KILLER_APP_URI',
    'KILLER_APP_TITLE',
    'ORG_SIGNUP_CONTACT',
    'ALLOW_MEMBER_SIGNUP'
]

# Emails
DEFAULT_FROM_EMAIL = env('DJANGO_FROM_EMAIL', 'no-reply@verifymyidentity.com')
DEFAULT_ADMIN_EMAIL = env('DJANGO_ADMIN_EMAIL',
                          'no-reply@verifymyidentity.com')

# The console.EmailBackend backend prints to the console.
# Redefine this for SES or other email delivery mechanism
EMAIL_BACKEND_DEFAULT = 'django_ses.SESBackend'
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', EMAIL_BACKEND_DEFAULT)

# Un-comment the next line to print emails to the console instead of using SES.
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MFA = True

SIGNUP_TIMEOUT_DAYS = 3
ORGANIZATION_NAME = "Verify My Identity"

# 4 MB Default
MAX_PROFILE_PICTURE_SIZE = env(
    'MAX_PROFILE_PICTURE_SIZE', str(4 * 1024 * 1024))

# Define individual identifier types
INDIVIDUAL_ID_TYPE_CHOICES = (
    ('PATIENT_ID_FHIR', 'Patient ID in FHIR'),
    ('MPI', 'Master Patient Index (Not FHIR Patient ID)'),
    ('SSN', 'Social Security Number'),
    ('MEDICAID_ID', 'Medicaid ID Number'),
    ('MEDICARE_HICN', 'Medicare HICN (Legacy)'),
    ('MEDICARE_ID', 'Medicare ID Number'),
    ('INSURANCE_ID', 'Insurance ID Number'),
    ('IHE_ID', 'Health Information Exchange ID'),
    ('NPI', 'National Provider Identifier'),
    ('UHI', 'Universal Health Identifier'),
)


# Define orgnization identifier types
ORGANIZATION_ID_TYPE_CHOICES = (
    ('FEIN', 'Federal Employer ID Number (Tax ID)'),
    ('NPI', 'National Provider Identifier'),
    ('OEID', 'Other Entity Identifier'),
    ('PECOS', 'PECOS Medicare ID'),
    ('UHI', 'Universal Health Identifier'),
)

DEFAULT_COUNTRY_CODE_FOR_INDIVIDUAL_IDENTIFIERS = env(
    'DEFAULT_COUNTRY_CODE_FOR_IDENTIFIERS', "US")

PHONENUMBER_DEFAULT_REGION = env('PHONENUMBER_DEFAULT_REGION', "US")

# Terms of service version
CURRENT_TOS_VERSION = env('CURRENT_TOS_VERSION', "1")

# Privacy Policy version
CURRENT_PP_VERSION = env('CURRENT_PP_VERSION', "1")

# Expire session on browser close.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Expire session. Default is 10 minutes: 10 * 60 seconds
SESSION_COOKIE_AGE = int(env('SESSION_COOKIE_AGE', int(30 * 60)))


# Pick a login template and title.
LOGIN_TEMPLATE_PICKER = {"default": 'login.html',
                         'share-my-health': 'login.html',
                         'hixny': 'login.html',
                         'healthy-together': 'login.html',
                         'new-york-department-of-health': 'login.html',
                         'new-york-my-medicaid': 'login.html',
                         'circulation': 'login.html'
                         }


IAL_EVIDENCE_CLASSIFICATIONS = [
    ('', 'No Identity Assurance evidence'),
    ('ONE-SUPERIOR-OR-STRONG+',
     'One Superior or Strong+ pieces of identity evidence'),
    ('ONE-STRONG-TWO-FAIR',
     'One Strong and Two Fair pieces of identity evidence'),
    ('TWO-STRONG',
     'Two Pieces of Strong identity evidence'),
    ('TRUSTED-REFEREE-VOUCH',
     'I am a Trusted Referee Vouching for this person'),
    ('KBA',
     'Knowledged-Based Identity Verification')]


IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_VALUE_1 = env(
    'IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_VALUE_1', "DRIVERS-LICENSE")
IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_DISPLAY_1 = env(
    'IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_DISPLAY_1', "Driver's License")


IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_VALUE_2 = env(
    'IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_VALUE_2', "MEDICAID-CARD")
IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_DISPLAY_2 = env(
    'IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_DISPLAY_2', "Medicaid card")

IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_VALUE_3 = env(
    'IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_VALUE_3', "MEDICARE-CARD")
IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_DISPLAY_3 = env(
    'IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_DISPLAY_3', "Medicare card")

IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_VALUE_4 = env(
    'IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_VALUE_4', "I9")
IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_DISPLAY_4 = env(
    'IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_DISPLAY_4', "I-9 Employee verification")


IAL_EVIDENCE_SUBCLASSIFICATIONS = []
IAL_EVIDENCE_SUBCLASSIFICATIONS.append(
    (IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_VALUE_1, IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_DISPLAY_1))
IAL_EVIDENCE_SUBCLASSIFICATIONS.append(
    (IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_VALUE_2, IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_DISPLAY_2))
IAL_EVIDENCE_SUBCLASSIFICATIONS.append(
    (IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_VALUE_3, IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_DISPLAY_3))
IAL_EVIDENCE_SUBCLASSIFICATIONS.append(
    (IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_VALUE_4, IAL_EVIDENCE_SUBCLASSIFICATION_CUSTOM_DISPLAY_4))


AUTO_IAL_2_DEFAULT_CLASSIFICATION = 'ONE-SUPERIOR-OR-STRONG+',
AUTO_IAL_2_DEFAULT_SUBCLASSIFICATION = env(
    'AUTO_IAL_2_DEFAULT_SUBCLASSIFICATION', "I9")
AUTO_IAL_2_DESCRIPTION = env(
    'AUTO_IAL_2_DESCRIPTION', "Documents verified by i9 employment")

LOGIN_RATELIMIT = env('LOGIN_RATELIMIT', '100/h')

# Change these for production
PASSPHRASE_SALT = env('PASSPHRASE_SALT', "FA6F747468657265616C706570706573")
PASSPHRASE_ITERATIONS = int(env('PASSPHRASE_ITERATIONS', "200"))
# These are added for portability to other cloud platforms.
# Note that instead these values can be passed as an IAM role.
# See
# https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', "set-your-own-id")
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', "set-your-own-key")
