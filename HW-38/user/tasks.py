from celery import shared_task
from user.models import User
from purchase.models import Purchase
from datetime import datetime

@shared_task
def i_print():
    print('Hello! I print any text')

@shared_task
def reciever(user_id):
    user = User.objects.get(id=user_id)
    purchase_count = Purchase.objects.filter(user=user).count()
    print(f"User {user.first_name} has made {purchase_count} purchases.")

@shared_task
def print_user_count():
    user_count = User.objects.count()
    print(f"{datetime.now()}: There are {user_count} User objects in the database.")