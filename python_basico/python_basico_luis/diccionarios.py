perfil = {
    "usuario" : "luchexs",
    "edad" : 16,
    "seguidores" : 1500,
    "juegos_favoritos" : ["Minecraft", "Fortnite", "Among Us"]
}
print(perfil["edad"])
perfil["seguidores"] += 20

print(perfil["seguidores"])

perfil["ciudad"] = "Tupiza"
print(perfil["ciudad"])

print(perfil.get("ciudad"))
print(perfil.get("pais", "No se encontró el país"))

print("############valores#########")
for clave, valor in perfil.items():
    print(f"{clave}: {valor}")
