mis_stickers = {"Messi", "Cristiano", "Neymar", "Mbappe", "Lewandowski"}

print ("---------------mis_stickers-----------------")
print (mis_stickers)

stickers_amigo = {"Messi", "Cristiano", "Mbappe", "Neymar", "lamine"}
print ("---------------stickers_amigo-----------------")
print(stickers_amigo)
print ("---------------operaciones-----------------")
print (mis_stickers & stickers_amigo) #interseccion
print (mis_stickers | stickers_amigo) #union
print (mis_stickers - stickers_amigo) #diferencia
print (stickers_amigo - mis_stickers) #diferencia
