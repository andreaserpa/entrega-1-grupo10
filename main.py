def leer_tareas():
    tareas = []
    with open("tareas.txt", "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(",")
            tarea = {
                "id":partes[0],
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
                "id":partes[0],
                "categoria": partes[1:]
            }
            recursos.append(recurso)
    return recursos

print(tareas)
print(recursos)