#método para listar las ventas
def listarCierres(clientes):
    print("Ventas:")
    contador =1 
    for cte in clientes:
        datos ="ID:{1}| Nombres:{2} | Apellidos:{3} | Dirección: {4})"
        print(datos.format(contador, cte[0], cte[1], cte[2], cte[3]))
        contador = contador+1
    print(" ")

