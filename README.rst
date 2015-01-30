===================================
django-based personal research blog
===================================


---------------
Installation
---------------
::

    git clone https://github.com/jasson15/rlog.git
    cd rlog
    python3 manage.py migrate


And then create a super user::

    python3 manage.py createsuperuser

After that, run the server::

    python3 manage.py runserver

Next login the admin page(http://localhost:8000/admin) to add polls

--------------
Dependency
--------------

1) Python 3.4
2) Django 1.7.4
3) django-bootstrap3
