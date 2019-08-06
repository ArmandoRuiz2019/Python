import random 

def checkSeleccionaCancionRandom(libreria):
	assert isinstance(libreria, dict)
	
	tituloCancion = random.choice(list(libreria.keys()))

	return tituloCancion

def iniciarPlayList(numeroCancion):
    for cancion in libreria: 

    	cancion = selecionaCancionRandom (libreria)
    if cancion not in playlist:
        	playlist[cancion]=libreria[cancion]
    else:
            iniciarPlayList()

    if len(libreria)==len(playlist):
             return playlist    	
playlist= {}
libreria = {"California_Uber_Alles.mp3": 
                {"track-number": 3, "artist": "Dead Kennedys", "album": "Dead Kennedys", "location": "./biblioteca/California_Uber_Alles.mp3"},
            "Seattle_Party": 
                {"track-number": 1, "artist": "Chastity Belt", "album": "No regrets", "location": "./biblioteca/Seattle_Party.flac"},
            "King_Kunta":
                {"track-number": 3, "artist": "Kendrick Lamar", "album": "To Pimp A Butterfly", "location": "./biblioteca/King_Kunta.mp3"}   
            }

##casos test##
print(checkSeleccionaCancionRandom(libreria))