# Django-crud-auth

## Deploy

- renden.com
- signUp con github
- service type "Web Services"
- SECRET_KEY = os.environ.get("SECRET_KEY", default="your secret key")
- DEBUG = 'RENDER' not in os.environ
-

```
  ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
 ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
```

- para archivos staticos `whitenoise`

- python manage.py collectstatic
