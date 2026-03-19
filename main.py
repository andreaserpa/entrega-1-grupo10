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
            "id_recurso": mejor_recurso["id"],
            "inicio": inicio,
            "fin": fin
        })

        tiempo_por_recurso[mejor_recurso["id"]] = fin
    
    return asignaciones
    
    


    