# main.py
import sys


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
    tiempo_por_recurso = {}
    asignaciones = []

    for r in recursos:
        tiempo_por_recurso[r["id"]] = 0

    for t in tareas:
        compatibles = []
        for r in recursos:
            if t["categoria"] in r["categorias"]:
                compatibles.append(r)

        mejor_recurso = compatibles[0]
        for r in compatibles:
            if tiempo_por_recurso[r["id"]] < tiempo_por_recurso[mejor_recurso["id"]]:
                mejor_recurso = r

        inicio = tiempo_por_recurso[mejor_recurso["id"]]
        fin = inicio + t["duracion"]

        asignaciones.append({
            "id_tarea": t["id"],
            "id_recurso": mejor_recurso["id"],
            "inicio": inicio,
            "fin": fin
        })

        tiempo_por_recurso[mejor_recurso["id"]] = fin

    return asignaciones


def escribir_output(asignaciones):
    with open("output.txt", "w", encoding="utf-8") as f:
        for a in asignaciones:
            f.write(f"{a['id_tarea']},{a['id_recurso']},{a['inicio']},{a['fin']}\n")


def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <makespan_objetivo>")
        return

    makespan_objetivo = int(sys.argv[1])

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