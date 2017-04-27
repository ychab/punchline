Punchline
=========

Collect and play with the best punchlines from various worlds like music,
politics, or literature.

Install
-------

::

    git clone
    cd punchline

    # For dev
    pip install -r requirements/dev.txt

    # For prod
    pip install -r requirements/prod.txt
    export DJANGO_SETTINGS_MODULE="project.settings.prod"

    cp src/project/settings/local.py.dist src/project/settings/local.py
    # edit it to fit your needs, like DB credentials

    python manage.py migrate
    python manage.py collectstatic

    python manage.py createsuperuser


