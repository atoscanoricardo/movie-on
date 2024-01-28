import requests


url_tiktok = "https://www.tiktok.com/tag/telocuento"  
headers_tiktok = {
    'Authorization': 'Bearer TU_TOKEN',  
}

response_tiktok = requests.get(url_tiktok, headers=headers_tiktok)

if response_tiktok.status_code == 200:
    videos = response_tiktok.json()['data']
    
    for video in videos:
        # Paso 3: Extraer información del video
        video_id = video['id']
        comments_url = f"https://api.tiktok.com/.../comments?video_id={video_id}"  # Reemplaza esto con la URL correcta
        response_comments = requests.get(comments_url, headers=headers_tiktok)
        
        if response_comments.status_code == 200:
            comments = response_comments.json()['data']
            
            for comment in comments:
                # Paso 4: Buscar en tu API de películas y series
                movie_name = comment['text']
                api_search_url = f"https://tu-api-peliculas-series.com/buscar?nombre={movie_name}"  # Reemplaza esto con la URL correcta
                response_api = requests.get(api_search_url)
                
                if response_api.status_code == 200:
                    movie_info = response_api.json()
                    # Paso 5: Procesar la respuesta y mostrar la información en tu aplicación
                    print(f"Información de la película/serie: {movie_info}")
                else:
                    print(f"Error al buscar en la API: {response_api.status_code}")
        else:
            print(f"Error al obtener comentarios: {response_comments.status_code}")
else:
    print(f"Error al obtener videos: {response_tiktok.status_code}")
