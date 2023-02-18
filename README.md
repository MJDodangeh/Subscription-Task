# Subscription-Task

Installation and run:
1- clone repository :
git clone https://github.com/MJDodangeh/Subscription-Task.git
Then enter the car traffic management folder and open cmd
2- create and activate virtualenv:
py -m virtualenv venv
.\venv\Scripts\activate
3- install packages:
pip install -r requirement.txt
4- Initialize database :
python manage.py makemigrations
5- migrate the database :
python manage.py migrate
6- run the application:
python manage.py runserver


The purpose of this task is to implement the cloud financial structure. In this way, the user subscribes to the system.
And after that, the user's credit is periodically reduced and an invoice is created for the user.

In short, the system works in such a way that the user can add a subscription. And the system should be with
Paying attention to the games that have a subscription, create an invoice for that user in time. The user can list
See his subscription and invoices.
Finally, the user should be able to get statistics from the system, how many have been invoiced and how much
has spent in the system.
