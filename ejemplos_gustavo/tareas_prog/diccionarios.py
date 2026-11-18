perfil = {
    "usuario" : "gamer_pro",
    "edad" : 25,
    "seguidores" : 320,
    "juegos_favoritos" : ["The Witcher 3", "Cyberpunk 2077", "Elden Ring"],
}

print(perfil["edad"])

perfil["seguidores"] += 26

print(perfil["seguidores"])

#agregar una clave nueva

perfil ["pais"] = "tupiza"

print(perfil["pais"])

#evitar un error si la clave es incorrecta

print(perfil.get("pais"))
print(perfil.get("ciudad", "no especificada"))



#mostrar los items
print("###############################")
for clave, valor in perfil.items():
    print(f"{clave}: {valor}")
print("###############################")
print("Claves:")
for clave in perfil.keys():

 print(perfil.keys())