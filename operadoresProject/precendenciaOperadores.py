# Ejemplo de una expresion 42//6+7*3-39
resutado0 = 42//6+7*3-39
resutado1 = (42//6)+7*3-39 # // prioridad 3
resutado2 = (42//6)+(7*3)-39 # * prioridad 3
resutado3 = ((42//6)+(7*3))-39 # + prioridad 4
resutado4 = (((42//6)+7*3))-39 # - prioridad 4

print(resutado4)