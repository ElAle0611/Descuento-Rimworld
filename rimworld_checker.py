import requests
import os
import smtplib
from email.message import EmailMessage

# Configuración de los AppIDs de RimWorld y sus DLCs
APPS_TO_CHECK = {
    "294100": "RimWorld",
    "1149640": "Royalty",
    "1392840": "Ideology",
    "1826960": "Biotech",
    "2384590": "Anomaly",
    "3022790": "Odyssey"
}

def enviar_alerta(mensaje_ofertas):
    # Recupera credenciales de los Secrets de GitHub
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
        print("Correo enviado con éxito.")
    except Exception as e:
        print(f"Error al enviar correo: {e}")

def check_steam_discounts():
    ofertas_encontradas = []
    
    for app_id, name in APPS_TO_CHECK.items():
        # 'cc=ar' asegura que los precios sean para la región de Argentina
        url = f"https://store.steampowered.com/api/appdetails?appids={app_id}&cc=ar"
        
        try:
            response = requests.get(url).json()
            if response[app_id]["success"]:
                data = response[app_id]["data"]
                
                if "price_overview" in data:
                    price_info = data["price_overview"]
                    discount = price_info["discount_percent"]
                    final_price = price_info["final_formatted"]
                    
                    if discount > 0:
                        ofertas_encontradas.append(f"✅ {name}: -{discount}% (Precio: {final_price})")
                        print(f"¡Oferta encontrada para {name}!")
                    else:
                        print(f"{name} está a precio completo.")
        except Exception as e:
            print(f"Error consultando {name}: {e}")

    # --- LÓGICA DE ENVÍO ---
    if ofertas_encontradas:
        cuerpo = "Hola,\n\nSteam detectó descuentos en los siguientes artículos de RimWorld:\n\n"
        cuerpo += "\n".join(ofertas_encontradas)
        cuerpo += "\n\n¡Es hora de comprar! 🛸"
        enviar_alerta(cuerpo)
    else:
        print("Hoy no hay descuentos. No se envió ningún correo.")

if __name__ == "__main__":
    check_steam_discounts()
