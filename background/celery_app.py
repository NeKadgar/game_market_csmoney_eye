import os
from celery import Celery
from kombu import Exchange, Queue
from kombu.common import Broadcast

app = Celery(__name__, include=['background.tasks'],)

app.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "amqp://localhost:5672/")
app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/1")

providers_exchange = Exchange("providers_exchange", type="direct")  # External connections queue
default_exchange = Exchange("default_exchange", type="direct")  # internal queue

app.conf.task_queues = (
    Queue("csmoney_queue", default_exchange, routing_key="csmoney_route"),
    Queue("items_base_queue", providers_exchange, routing_key="items_base_route"),  # noqa
    Broadcast('broadcast_provider', routing_key='broadcast_provider'),
)
