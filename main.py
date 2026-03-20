# main.py

def leer_tareas():
    tareas = []
    with open("tareas.txt", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            tarea = {
                "id": partes[0],
                "duracion": int(partes[1]),
                "categoria": partes[2]
            }
            tareas.append(tarea)
    return tareas


def leer_recursos():
    recursos = []
    with open("recursos.txt", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            recurso = {
                "id": partes[0],
                "categorias": partes[1:]
            }
            recursos.append(recurso)
    return recursos


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
            "id_recurso": mejor_recurso["id"],
            "inicio": inicio,
            "fin": fin
        })

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