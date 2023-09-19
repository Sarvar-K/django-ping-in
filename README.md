Plug-in to ping current Django project
=======================
Library provides endpoint to ping the Django server of the project where the library is installed.

Installation
----------------
```commandline
 pip install git+https://github.com/Sarvar-K/django-ping-in
```

In _requirements.txt_ file
```txt
git+https://github.com/Sarvar-K/django-ping-in
```
**Installation in Docker**: If installing via *pip install*, you will require *git* in image.

Setup
--------------
Add 'ping_in' to your INSTALLED_APPS in settings.py.
```python
INSTALLED_APPS = [
    ...
    'ping_in',
]
```

Add _ping_urls_ to your project's _urls.py_, preferably in the beginning of _urlpatterns_ (check ping url first), like so:
```python
...
from ping_in.urls import urlpatterns as ping_urls

urlpatterns = [
    path('your-URI-key/', include(ping_urls)),
    path('admin/', admin.site.urls),
    ...
]
```



Usage
---------------------------------

Ping endpoint is available at:
```html
/your-URI-key/ping
```

Successful response is of Content-Type: text/html, status code 200 and response body "OK".
