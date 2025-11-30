from django.core.management.base import BaseCommand
from rectangles.utils import Rectangle

class Command(BaseCommand):
    help = "Demonstrate Rectangle iteration"

    def handle(self, *args, **options):
        r = Rectangle(10, 5)
        print("Rectangle:", r)
        print("Iterating:")
        for item in r:
            print(" ->", item)

        print("\nIterating again:")
        for item in r:
            print(" ->", item)
