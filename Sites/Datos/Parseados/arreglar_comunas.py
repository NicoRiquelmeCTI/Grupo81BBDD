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

with open("proyectos_2.csv", "r", encoding="utf-8") as file_P:
    minas = dict()
    vertederos = list()
    centrales = dict()
    for linea in file_P:
        p = linea.strip().split(";")
        p1 = p[0]
        p2 = p[8]
        p3 = p[9]
        if p2 != "-":
            minas[p1] = p2
        if p3 != "-":
            centrales[p1] = p3
        elif p2 == "-" and p3 == "-":
            vertederos.append(p1)
        
with open("extracciones.csv", "w", encoding="utf-8") as file_e:
    file_e.write("id,tipo_extraccion" + "\n")
    for id_ in list(minas.keys()):
        if id_ != "id":
            linea = id_ + "," + minas[id_]
            file_e.write(linea + "\n")

with open("centrales.csv", "w", encoding="utf-8") as file_c:
    file_c.write("id,tipo_generacion" + "\n")
    for id_ in list(centrales.keys()):
        if id_ != "id":
            linea = id_ + "," + centrales[id_]
            file_c.write(linea + "\n")

with open("vertederos.csv", "w", encoding="utf-8") as file_v:
    file_v.write("id" + "\n")
    for i in range(1, len(vertederos)):
        file_v.write(vertederos[i] + "\n")

