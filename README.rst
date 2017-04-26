Install
-------

::

    cd <project>

    # For dev
    pip install -r requirements/dev.txt
    pip install -e .

    # For prod
    pip install -r requirements/prod.txt
    pip install .
    export DJANGO_SETTINGS_MODULE="project.settings.prod"

    cp src/project/settings/local.py.dist src/project/settings/local.py
    # edit it ti fit your needs

    cd src
    python manage.py migrate
    python manage.py collectstatic

    python manage.py createsuperuser


