import os
import smtplib
from email.message import EmailMessage

def enviar_alerta(mensaje_ofertas):
    # Recuperamos los datos de los secretos de GitHub
    user = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    receiver = os.getenv("EMAIL_RECEIVER")

    msg = EmailMessage()
    msg.set_content(mensaje_ofertas)
    msg["Subject"] = "🚨 ¡OFERTA DETECTADA EN RIMWORLD! 🚨"
    msg["From"] = user
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(user, password)
            server.send_message(msg)
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

# ... (en tu lógica de checking)
ofertas_encontradas = []

# Dentro del bucle de apps:
if discount > 0:
    ofertas_encontradas.append(f"- {name}: {discount}% de descuento. Precio: {final_price}")

# Al final del script:
if ofertas_encontradas:
    cuerpo_mail = "Se detectaron los siguientes descuentos en Steam:\n\n" + "\n".join(ofertas_encontradas)
    enviar_alerta(cuerpo_mail)
