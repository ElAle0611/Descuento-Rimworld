- RimWorld Price Monitor
Un script sencillo en Python para no tener que revisar Steam todos los días. El bot vigila los precios de RimWorld y sus DLCs, y me avisa al mail solo cuando hay una oferta real.

- Cómo funciona

El sistema es 100% autónomo y corre en la nube:

Extracción: Consulta la API oficial de Steam Store cada mediodía (Hora ARG).

Lógica: Compara el precio base con el precio actual.

Alerta: Si detecta un descuento >0%, dispara un correo vía SMTP (Gmail).

Contenido Monitoreado

AppID	Contenido	Región
294100	RimWorld (Base)	Argentina (cc=ar)
1149640	Royalty	Argentina (cc=ar)
1392840	Ideology	Argentina (cc=ar)
1826960	Biotech	Argentina (cc=ar)
2384590	Anomaly	Argentina (cc=ar)
3022790	Odyssey	Argentina (cc=ar)


-Stack Tecnológico


Python 3.10 (Scripting y automatización).

GitHub Actions (Orquestador / Cron Job en la nube).

Steam API (Fuente de datos).

Nota personal: RimWorld casi nunca tiene descuentos grandes. Este proyecto aplica un poco de filosofía estoica: controlar la información para actuar con sabiduría (y ahorro) cuando llegue el momento.

- ¿Cómo lo uso?

Si querés replicarlo, solo necesitás:

Clonar el repo.

Cargar tus secretos en GitHub (EMAIL_USER, EMAIL_PASS, EMAIL_RECEIVER).

Activar el Workflow en la pestaña Actions.

De nada, creo que mas claro no pude ser, alguna duda, escribeme.
