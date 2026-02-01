import requests

# Lista de AppIDs a monitorear
APPS_TO_CHECK = {
    "294100": "RimWorld",
    "1149640": "Royalty",
    "1392840": "Ideology",
    "1826960": "Biotech",
    "2384590": "Anomaly",
    "3022790": "Odyssey"
}

def check_steam_discounts():
    for app_id, name in APPS_TO_CHECK.items():
        # URL de la API de la tienda de Steam
        url = f"https://store.steampowered.com/api/appdetails?appids={app_id}&cc=ar" # 'cc=ar' para precios en Argentina
        
        try:
            response = requests.get(url).json()
            
            if response[app_id]["success"]:
                data = response[app_id]["data"]
                
                # Verificar si el juego tiene un apartado de precios
                if "price_overview" in data:
                    price_info = data["price_overview"]
                    discount = price_info["discount_percent"]
                    final_price = price_info["final_formatted"]
                    
                    if discount > 0:
                        print(f"¡OFERTA! {name} tiene un -{discount}% de descuento. Precio: {final_price}")
                    else:
                        print(f"{name} está a precio completo: {final_price}")
                else:
                    print(f"{name} no tiene precio disponible o es gratuito.")
            else:
                print(f"No se pudo obtener información para {name}.")
                
        except Exception as e:
            print(f"Error al consultar {name}: {e}")

if __name__ == "__main__":
    check_steam_discounts()