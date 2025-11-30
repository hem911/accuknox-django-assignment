import threading
from django.dispatch import Signal, receiver
from django.db import transaction
from .models import HandlerCreatedModel

custom_signal = Signal()

_demo_store = {
    "sync_calls": [],
    "thread_ids": [],
}

@receiver(custom_signal)
def sync_handler(sender, **kwargs):
    payload = kwargs.get("payload")
    _demo_store["sync_calls"].append(("handler_called", payload))
    _demo_store["thread_ids"].append(("handler_thread", threading.get_ident()))

@receiver(custom_signal)
def db_handler(sender, **kwargs):
    note = kwargs.get("payload", "from_handler")
    HandlerCreatedModel.objects.create(note=note)

def get_demo_store():
    return _demo_store

def reset_demo_store():
    _demo_store["sync_calls"].clear()
    _demo_store["thread_ids"].clear()
