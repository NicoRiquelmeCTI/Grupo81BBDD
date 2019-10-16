with open("comunas.csv", "r", encoding="utf-8") as file_c:
    comunas = dict()
    for f in file_c:
        [c1, c2, c3, _] = f.strip().split(";")
        if c3 != "comuna":
            comunas[c3] = c1

with open("proyectos_2.csv", "r", encoding="utf-8") as file_p:
    proyectos = list()
    for f in file_p:
        [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11] = f.strip().split(";")
        if p2 != "tipo":
            id_c = comunas[p6]
            if p8 == "si":
                linea = p1 + ";" + p3 + ";" + p4 + ";" + p5 + ";" + p7 + ";" + "true" + ";" + p2 + ";" + id_c
            else:
                linea = p1 + ";" + p3 + ";" + p4 + ";" + p5 + ";" + p7 + ";" + "false" + ";" + p2 + ";" + id_c
       
        else:
            linea = p1 + ";" + p3 + ";" + p4 + ";" + p5 + ";" + p7 + ";" + p8 + ";" + p2 + ";" + "id_c"
        proyectos.append(linea)

with open("proyectos.csv", "w", encoding="utf-8") as file:
    for linea in proyectos:
        file.write(linea +"\n")
