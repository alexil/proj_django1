from __future__ import absolute_import

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.views.decorators.http import require_GET, require_POST


@require_GET
def process_count_2(request):
    # import thread
    # thread.start_new_thread(ccc())
    # thread.exit_thread()

    from django.core.mail import EmailMultiAlternatives

    subject, from_email, to = 'hello', 'From Don\'t Reply do_not_replay@domain.com', ['miil@gmx.com','scourgecp@gmail.com']
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    import threading


    t1 = threading.Thread(target=ccc, args=(), kwargs={})
    t1.start()
    return HttpResponse("GYGY")

# @require_GET
# def process_count2(request):
def ccc():
    from django.db import connection
    from django.db.utils import OperationalError
    import time

    cursor = connection.cursor()

    while True:
        try:
            ### Show today's date and time ##
            print "Current date & time " + time.strftime("%c")

            #### Delay for 1 seconds ####
            time.sleep(1)

            # kill our own database connection
            print cursor.execute('SELECT 1;')
            print "OK"


        except OperationalError:
            if connection:
                connection.close()
                cursor = connection.cursor()
            print cursor.execute('SELECT 1;')
            print " ----------------------------------------err 1"

        except Exception:
            connection.close()
            cursor = connection.cursor()
            print "======================================== err GENERAL"

    return HttpResponse("GYGY")

