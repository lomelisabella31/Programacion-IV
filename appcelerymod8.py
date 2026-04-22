from celery import Celery
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

celery = Celery(
    "tareas",
    broker=os.getenv("CELERY_BROKER_URL")
)

@celery.task
def enviar_correo(asunto, titulo):
    try:
        servidor = smtplib.SMTP(os.getenv("MAIL_SERVER"), int(os.getenv("MAIL_PORT")))
        servidor.starttls()

        servidor.login(os.getenv("MAIL_USERNAME"), os.getenv("MAIL_PASSWORD"))

        mensaje = f"Subject: {asunto}\n\nSe hizo accion con el libro: {titulo}"

        servidor.sendmail(
            os.getenv("MAIL_USERNAME"),
            os.getenv("MAIL_USERNAME"),
            mensaje
        )

        servidor.quit()
    except:
        print("error enviando correo")
