# main.py
import sys
from typing import Any

def leer_tareas(nombre_archivo: str) -> list[dict[str,Any]]:
    tareas: list[dict[str,Any]] = []
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            tarea = {
                "id": partes[0],
                "duracion": int(partes[1]),
                "categoria": partes[2]
            }
            tareas.append(tarea)
    return tareas


def leer_recursos(nombre_archivo: str) -> list[dict[str,Any]]:
    recursos: list[dict[str,Any]] = []
    with open("recursos.txt", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            recurso = {
                "id": partes[0],
                "categorias": partes[1:]
            }
            recursos.append(recurso)
    return recursos


def planificar_tareas(tareas: list[dict[str, Any]], recursos: list[dict[str, Any]]) -> list[dict[str, Any]]:
    tiempo_por_recurso: dict[str, int] = {r["id"]: 0 for r in recursos}
    asignaciones: list[dict[str, Any]] = []

    for t in tareas:
        compatibles = [r for r in recursos if t["categoria"] in r["categorias"]]

        mejor_recurso = min(compatibles, key=lambda r: tiempo_por_recurso[r["id"]])
        
        id_r = mejor_recurso["id"]
        inicio = tiempo_por_recurso[id_r]
        fin = inicio + t["duracion"]

        asignaciones.append({
            "id_tarea": t["id"],
            "id_recurso": id_r,
            "inicio": inicio,
            "fin": fin
        })
        tiempo_por_recurso[id_r] = fin 
    
    return asignaciones


def escribir_output(asignaciones: list[dict[str, Any]])-> None:
    with open("output.txt", "w", encoding="utf-8") as f:
        for a in asignaciones:
            f.write(f"{a['id_tarea']},{a['id_recurso']},{a['inicio']},{a['fin']}\n")


def main()-> None:
    if len(sys.argv) != 4:
        print("Uso: python main.py <makespan_objetivo>")
        return

    makespan_objetivo = int(sys.argv[1])
    archivo_t = sys.argv[2]
    archivo_r = sys.argv[3]


    tareas = leer_tareas(archivo_t)
    recursos = leer_recursos(archivo_r)
    asignaciones = planificar_tareas(tareas, recursos)
    escribir_output(asignaciones)

    print(f"Planificacion completada usando {archivo_t} y {archivo_r}")
    print(f"Makespan objetivo:{makespan_objetivo}")
    print("Se generó output.txt correctamente")


if __name__ == "__main__":
    main()