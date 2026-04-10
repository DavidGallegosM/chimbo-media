import yt_dlp
import os
from logo import logo

print(logo)
print("by - makima (Enhanced Version)\n")

while True:
    enlace = input("Ingresa el enlace de youtube => ")
    print("¿Qué formato prefieres?\n1. MP3 (Alta Calidad + Portada)\n2. MP4 (Video)")
    formato = input("==> ")

    ruta = input("Pega la ruta de la carpeta (Enter para carpeta actual): ").strip()
    if not ruta or not os.path.exists(ruta):
        ruta = "."

    # Configuración base
    opciones_base = {
        'outtmpl': f'{ruta}/%(title)s.%(ext)s',
        'writethumbnail': True, # Descarga la imagen de portada
    }

    if formato == "1":
        print("Descargando MP3 en alta calidad (320kbps) con metadatos...")
        opciones_base.update({
            'format': 'bestaudio/best',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320', # Máxima calidad de audio
                },
                {
                    'key': 'EmbedThumbnail', # Inserta la foto en el MP3
                },
                {
                    'key': 'FFmpegMetadata', # Inserta artista, título, etc.
                    'add_metadata': True,
                },
            ],
        })
    
    elif formato == "2":
        print("Descargando MP4...")
        opciones_base.update({
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        })
    else:
        print("Opción no válida.")
        continue

    try:
        with yt_dlp.YoutubeDL(opciones_base) as ydl:
            ydl.download([enlace])
        print("--- Descarga completa con éxito ---")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    volver_a_descargar = input("\n¿Realizar otra descarga? Si/No => ").strip().lower()
    if volver_a_descargar in ["no", "n"]:
        print("¡Hasta luego!")
        break
    else:
        print("\n" + "="*30 + "\n")