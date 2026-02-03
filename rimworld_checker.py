import requests
import os
import smtplib
from email.message import EmailMessage

# Lista de AppIDs a monitorear
APPS_TO_CHECK = {
    "294100": "RimWorld",
    "1149640": "Royalty",
    "1392840": "Ideology",
    "1826960": "Biotech",
    "2384590": "Anomaly",
    "3022790": "Odyssey"
}

def enviar_alerta(mensaje_ofertas):
    user = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    receiver = os.getenv("EMAIL_RECEIVER")

    msg = EmailMessage()
    msg.set_content(mensaje_ofertas)
    msg["Subject"] = "🚨 PRUEBA: Monitor de RimWorld"
    msg["From"] = user
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(user, password)
            server.send_message(msg)
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

def check_steam_discounts():
    ofertas_encontradas = []
    
    for app_id, name in APPS_TO_CHECK.items():
        url = f"https://store.steampowered.com/api/appdetails?appids={app_id}&cc=ar"
        try:
            response = requests.get(url).json()
            if response[app_id]["success"]:
                data = response[app_id]["data"]
                if "price_overview" in data:
                    # AQUÍ SE DEFINE 'discount'
                    price_info = data["price_overview"]
                    discount = price_info["discount_percent"]
                    final_price = price_info["final_formatted"]
                    
                    if discount > 0:
                        ofertas_encontradas.append(f"- {name}: {discount}% OFF ({final_price})")
        except Exception as e:
            print(f"Error consultando {name}: {e}")

    # --- LÓGICA DE PRUEBA ---
    # Cambiá esto cuando confirmes que el mail llega:
    if not ofertas_encontradas:
        enviar_alerta("Prueba de conexión: El script corrió pero no encontró ofertas reales hoy.")
    else:
        cuerpo = "¡Hay ofertas!\n\n" + "\n".join(ofertas_encontradas)
        enviar_alerta(cuerpo)

if __name__ == "__main__":
    check_steam_discounts()
