from celery import Celery


def make_celery(flask_app):
    celery = Celery(
        flask_app.import_name,
        result_backend=flask_app.config.pop('CELERY_RESULT_BACKEND'),
        broker=flask_app.config.pop('CELERY_BROKER_URL'),
        include=['background.tasks'],
    )
    celery.conf.update(flask_app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
