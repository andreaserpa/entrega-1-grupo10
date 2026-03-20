<<<<<<< HEAD
# main.py

=======
>>>>>>> d927c52021ce9a72cbeb3584e29e4930164098ed
def leer_tareas():
    tareas = []
    with open("tareas.txt", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            tarea = {
<<<<<<< HEAD
                "id": partes[0],
=======
                "id":partes[0],
>>>>>>> d927c52021ce9a72cbeb3584e29e4930164098ed
                "duracion": int(partes[1]),
                "categoria": partes[2]
            }
            tareas.append(tarea)
    return tareas

<<<<<<< HEAD

=======
>>>>>>> d927c52021ce9a72cbeb3584e29e4930164098ed
def leer_recursos():
    recursos = []
    with open("recursos.txt", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            recurso = {
<<<<<<< HEAD
                "id": partes[0],
                "categorias": partes[1:]
=======
                "id":partes[0],
                "categoria": partes[1:]
>>>>>>> d927c52021ce9a72cbeb3584e29e4930164098ed
            }
            recursos.append(recurso)
    return recursos

<<<<<<< HEAD

def planificar_tareas(tareas, recursos):
    asignaciones = []
    tiempo_recurso = {}

    # Inicializa tiempo disponible de cada recurso
    for recurso in recursos:
        tiempo_recurso[recurso["id"]] = 0

    # Asigna tareas al recurso compatible más libre
    for tarea in tareas:
        compatibles = [r for r in recursos if tarea["categoria"] in r["categorias"]]

        # Elegir el recurso con menor tiempo disponible
        mejor_recurso = min(compatibles, key=lambda r: tiempo_recurso[r["id"]])

        inicio = tiempo_recurso[mejor_recurso["id"]]
        fin = inicio + tarea["duracion"]

        asignaciones.append({
            "id_tarea": tarea["id"],
=======
def asignacion_tareas(tareas, recursos):
    tiempo_por_recurso = {}
    asignaciones=[]
    for r in recursos: 
        tiempo_por_recurso[r["id"]]=0

    for t in tareas:
        compatibles = []
        for r in recursos:
            if t["categoria"] in r["categoria"]:
                compatibles.append(r)

        mejor_recurso = compatibles[0] 
        for recurso in compatibles:
            if tiempo_por_recurso[recurso["id"]] < tiempo_por_recurso[mejor_recurso["id"]]:
                    mejor_recurso = recurso

        inicio = tiempo_por_recurso[mejor_recurso["id"]]
        fin = inicio + t["duracion"]

        asignaciones.append({
            "id_tarea": t["id"],
>>>>>>> d927c52021ce9a72cbeb3584e29e4930164098ed
            "id_recurso": mejor_recurso["id"],
            "inicio": inicio,
            "fin": fin
        })

<<<<<<< HEAD
        # Actualiza el tiempo disponible del recurso
        tiempo_recurso[mejor_recurso["id"]] = fin

    return asignaciones


def escribir_output(asignaciones):
    with open("output.txt", "w", encoding="utf-8") as f:
        for a in asignaciones:
            f.write(f"{a['id_tarea']},{a['id_recurso']},{a['inicio']},{a['fin']}\n")


def main():
    # Para Spyder: hardcodeamos makespan objetivo
    makespan_objetivo = 10

    tareas = leer_tareas()
    recursos = leer_recursos()
    asignaciones = planificar_tareas(tareas, recursos)
    escribir_output(asignaciones)

    print("Makespan objetivo recibido:", makespan_objetivo)
    print("Tareas asignadas:")
    for a in asignaciones:
        print(a)
    print("Se generó output.txt correctamente")


if __name__ == "__main__":
    main()
=======
        tiempo_por_recurso[mejor_recurso["id"]] = fin
    
    return asignaciones
    
    


    
>>>>>>> d927c52021ce9a72cbeb3584e29e4930164098ed




def main():
    tareas = leer_tareas()
    recursos = leer_recursos()
    if len(sys.argv) != 2:
        print("Uso: python main.py <makespan_objetivo>")
        return
        makespan_objetivo = int(sys.argv[1])
tareas = leer_tareas()
recursos = leer_recursos()
asignaciones = asignacion_tareas(tareas, recursos)
def escribir output(asignaciones):
    with open("output.txt", "w", encoding = "utf-8") as f:
        for a in asignaciones:
            f.write(f"{a['id_tarea']},{a['id_recurso']},{a['inicio']},{a['fin']}\n")

print("Makespan objetivo recibido:", makespan_objetivo)
print("Se genero output.txt correctamente")
