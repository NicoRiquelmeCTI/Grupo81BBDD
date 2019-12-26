
import csv
import ast

with open("Datos Proyecto - Proyectos.csv", 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',', skipinitialspace=True, quotechar='"')
    with open('proyectos_2.csv', 'w') as f:
     for linea in csv_reader:
        for palabra in linea:
            palabra2 = palabra.replace('ñ', 'n')
            palabra2 = palabra2.replace('á', 'a')
            palabra2 = palabra2.replace('é', 'e')
            palabra2 = palabra2.replace('í', 'i')
            palabra2 = palabra2.replace('ó', 'o')
            palabra2 = palabra2.replace('ú', 'u')
            palabra2 = palabra2.replace('Ñ', 'N')
            palabra2 = palabra2.replace('Á', 'A')
            palabra2 = palabra2.replace('É', 'E')
            palabra2 = palabra2.replace('Í', 'I')
            palabra2 = palabra2.replace('Ó', 'O')
            palabra2 = palabra2.replace('ü', 'u')
            palabra2 = palabra2.replace('ç', 'c')
            palabra2 = palabra2.replace('ç', 'c')
            palabra2 = palabra2.replace('ç', 'c')
            palabra2 = palabra2.replace(',', '')
            palabra2 = palabra2.replace("'", '')
            palabra2 = palabra2.replace("/", '-')
            palabra2 = palabra2.replace("NA", '0')
            palabra2 = palabra2.replace(".", '')
            for i in range(0, len(linea)):
                if linea[i] == palabra:
                    linea[i] = palabra2
        linea = ','.join(linea)

        f.write(linea + "\n")



with open('Datos Proyecto - Recursos.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',', skipinitialspace=True, quotechar='"')
    with open('recursos_2.csv', 'w') as f:
     for linea in csv_reader:
        for palabra in linea:
            palabra2 = palabra.replace('ñ', 'n')
            palabra2 = palabra2.replace('á', 'a')
            palabra2 = palabra2.replace('é', 'e')
            palabra2 = palabra2.replace('í', 'i')
            palabra2 = palabra2.replace('ó', 'o')
            palabra2 = palabra2.replace('ú', 'u')
            palabra2 = palabra2.replace('Ñ', 'N')
            palabra2 = palabra2.replace('Á', 'A')
            palabra2 = palabra2.replace('É', 'E')
            palabra2 = palabra2.replace('Í', 'I')
            palabra2 = palabra2.replace('Ó', 'O')
            palabra2 = palabra2.replace('ü', 'u')
            palabra2 = palabra2.replace('ç', 'c')
            palabra2 = palabra2.replace('ç', 'c')
            palabra2 = palabra2.replace('ç', 'c')
            palabra2 = palabra2.replace(',', '')
            palabra2 = palabra2.replace("'", '')
            palabra2 = palabra2.replace("/", '-')
            palabra2 = palabra2.replace("NA", '0')
            for i in range(0, len(linea)):
                if linea[i] == palabra:
                    linea[i] = palabra2
        linea = ','.join(linea)
        f.write(linea + "\n")


with open("Datos Proyecto - Socios.csv", 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',', skipinitialspace=True, quotechar='"')
    with open('socios_2.csv', 'w') as f:
     for linea in csv_reader:
        for palabra in linea:
            palabra2 = palabra.replace('ñ', 'n')
            palabra2 = palabra2.replace('á', 'a')
            palabra2 = palabra2.replace('é', 'e')
            palabra2 = palabra2.replace('í', 'i')
            palabra2 = palabra2.replace('ó', 'o')
            palabra2 = palabra2.replace('ú', 'u')
            palabra2 = palabra2.replace('Ñ', 'N')
            palabra2 = palabra2.replace('Á', 'A')
            palabra2 = palabra2.replace('É', 'E')
            palabra2 = palabra2.replace('Í', 'I')
            palabra2 = palabra2.replace('Ó', 'O')
            palabra2 = palabra2.replace('ü', 'u')
            palabra2 = palabra2.replace('ç', 'c')
            palabra2 = palabra2.replace('ç', 'c')
            palabra2 = palabra2.replace('ç', 'c')
            palabra2 = palabra2.replace(',', '')
            palabra2 = palabra2.replace("'", '')
            palabra2 = palabra2.replace("/", '-')
            palabra2 = palabra2.replace("NA", '0')
            for i in range(0, len(linea)):
                if linea[i] == palabra:
                    linea[i] = palabra2
        linea = ','.join(linea)

        f.write(linea + "\n")
# with open("probar.csv", 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter = ',', skipinitialspace=True, quotechar='"')
#     with open('probar2.csv', 'w') as f:
#      for linea in csv_reader:
#         for palabra in linea:
#             palabra2 = palabra.replace('ñ', 'n')
#             palabra2 = palabra2.replace('á', 'a')
#             palabra2 = palabra2.replace('é', 'e')
#             palabra2 = palabra2.replace('í', 'i')
#             palabra2 = palabra2.replace('ó', 'o')
#             palabra2 = palabra2.replace('ú', 'u')
#             palabra2 = palabra2.replace('Ñ', 'N')
#             palabra2 = palabra2.replace('Á', 'A')
#             palabra2 = palabra2.replace('É', 'E')
#             palabra2 = palabra2.replace('Í', 'I')
#             palabra2 = palabra2.replace('Ó', 'O')
#             palabra2 = palabra2.replace('ü', 'u')
#             palabra2 = palabra2.replace('ç', 'c')
#             palabra2 = palabra2.replace('ç', 'c')
#             palabra2 = palabra2.replace('ç', 'c')
#             palabra2 = palabra2.replace(',', '')
#             palabra2 = palabra2.replace("'", '')
#             for i in range(0, len(linea)):
#                 if linea[i] == palabra:
#                     linea[i] = palabra2
#         linea = ','.join(linea)
#
#         f.write(linea + "\n")