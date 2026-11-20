perfil = {
    "usuario": "gamer_bolivia",
    "edad": 15,
    "seguidores": 320,
    "juegos_favoritos": ["Minecraft", "Fortnite"]
}

print(perfil["edad"])            # Acceder por clave

perfil["seguidores"] += 10          # Modificar un valor
#seguidores = seguidores + 10

print (perfil["seguidores"])

# Agregar una clave nueva
perfil["ciudad"] = "Tupiza" 

print (perfil["ciudad"])
# Evita error si la clave no existe
print (perfil.get("ciudad"))
print(perfil.get("pais", "No especificado"))



# Mostrar los Items
print ("####################valores##################")
for clave, valor in perfil.items():
    print(f"{clave}: {valor}")

print (perfil.keys)