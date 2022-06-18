from datetime import timedelta
from kombu import Exchange, Queue

from background import make_celery
from main import create_app


app = make_celery(create_app())


default_exchange = Exchange("default_csmoney", type="direct")  # Internal connections queue
providers_exchange = Exchange("providers_exchange", type="direct")  # External connections queue

app.conf.task_queues = (
    Queue("csmoney_queue", default_exchange, routing_key="csmoney_route"), # noqa
)

app.conf.beat_schedule = {
    # Executes every 2 hours
    "parse": {
        "task": "background.tasks.parser.parse",
        "schedule": timedelta(hours=3),
        'options': {
            'queue': 'csmoney_queue',
            # 'expires': timedelta(seconds=5),
        },
    },
}
