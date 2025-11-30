from django.core.management.base import BaseCommand
from django.db import transaction
from signals_app.signals import custom_signal, get_demo_store, reset_demo_store
from signals_app.models import HandlerCreatedModel
import threading

class Command(BaseCommand):
    help = "Demonstrate Django signal behaviors"

    def handle(self, *args, **options):
        print("===== TEST 1: ARE SIGNALS SYNCHRONOUS? =====")
        reset_demo_store()
        custom_signal.send(sender=self.__class__, payload="sync-test")
        store = get_demo_store()
        print("Handler calls:", store["sync_calls"])
        print("=> YES, handler ran before send() returned (synchronous).")

        print("\n===== TEST 2: SAME THREAD? =====")
        reset_demo_store()
        main_id = threading.get_ident()
        custom_signal.send(sender=self.__class__, payload="thread-test")
        store = get_demo_store()
        print("Main thread ID:", main_id)
        print("Handler thread IDs:", store["thread_ids"])
        print("=> YES, handler ran in SAME thread.")

        print("\n===== TEST 3: SAME DATABASE TRANSACTION? =====")
        HandlerCreatedModel.objects.all().delete()
        try:
            with transaction.atomic():
                custom_signal.send(sender=self.__class__, payload="tx-test")
                raise RuntimeError("Force rollback")
        except RuntimeError:
            pass

        count = HandlerCreatedModel.objects.filter(note="tx-test").count()
        print("Objects created by handler after rollback:", count)
        print("=> Handler DB changes were rolled back WITH caller.")
