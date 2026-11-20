print("------MIS STICKERS---------")
mis_stickers = {"Messi", "Mbappé", "Haaland", "Messi", "Vinícius"}
print(mis_stickers)       # "Messi" aparece solo una vez
#mis_stickers.remove

print("------ STICKERS AMIGO---------")
stickers_amigo = {"Haaland", "Bellingham", "Vinícius", "Pedri"}
print (stickers_amigo)
# Operaciones de conjuntos (¡como en matemáticas!)
print("------operaciones-----------")
print(mis_stickers & stickers_amigo)   # Los que tenemos los dos (intersección)
print(mis_stickers | stickers_amigo)   # Todos juntos (unión)
print(mis_stickers - stickers_amigo)   # Los que solo tengo yo (diferencia)
print(stickers_amigo - mis_stickers)

#mis_stickers.add("Pedri")
#print("Messi" in mis_stickers)         # ¿Lo tengo? → True