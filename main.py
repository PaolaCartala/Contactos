import os # esta es la librería que se usará para administrar los archivos

# -- Valores que se usarán constantemente --
CARPETA = "Contactos/" # la carpeta Contactos/ será referida como CARPETA
EXTENSION = ".txt" # la extension de los archivos utilizados siempre será .txt

# --- Clase Contacto ---
class Contacto: # estos serán los datos que se guardarán en los archivos
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

# --- Función principal que contendrá todas las opciones ---
def app():
    crear_directorio()
    mostrar_menu() # muestra el menú de opciones

    # --- Elección de opciones por parte del usuario ---
    preguntar = True
    while preguntar:
        opcion = int(input("Seleccione una opción: \n")) 
        # -- Ejecutar opciones --
        if opcion == 1:
            agregar_contacto()
            preguntar = False # con este cambio no preguntará más una vez elegida una opción
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        elif opcion == 6:
            preguntar = False # salir del bucle sin hacer nada
        else:
            print("Opción no válida, intente de nuevo") # en caso de que se ingrese un número que no esté entre las opciones, volverá a preguntar qué opción quiere elegir

# --- Crea el directorio donde se guardarán los contactos ---
def crear_directorio():
    if not os.path.exists(CARPETA): # si la carpeta no existe, la creamos
        os.makedirs(CARPETA)

# --- Muestra el menú de opciones ---
def mostrar_menu():
    print("Seleccione del menú lo que desea hacer:")
    print("1) Agregar Nuevo Contacto")
    print("2) Editar Contacto")
    print("3) Ver Contactos")
    print("4) Buscar Contacto")
    print("5) Eliminar Contacto")
    print("6) Salir del Programa")

# --- C CREATE / Agregar contactos ---
def agregar_contacto():
    print("Escribe los datos para agregar el nuevo contacto:")
    nombre_contacto = input("Nombre del Contacto:\n").capitalize() # utiliza el método capitalize() para poner en mayúscula la primera letra de cada palabra ingresada, por si el usuario las ingresa con minúscula
    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION) # valida si el archivo ya existe antes de crearlo para que no se reescriba
    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, "w", encoding="utf8") as archivo: # abre el archivo con permiso de escritura
            telefono_contacto = int(input("Agrega el teléfono del contacto:\n"))
            categoria_contacto = input("Agrega la categoría del contacto:\n").capitalize()

            # instancia la clase Contacto
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto) # los argumentos serán los datos que ingresó el usuario
            
            # write escribirá los datos del objeto en archivo
            archivo.write ("Nombre: " + contacto.nombre + "\n")
            archivo.write ("Telefono: " + str(contacto.telefono) + "\n")
            archivo.write ("Categoria: " + contacto.categoria + "\n")

            # muestra un mensaje de exito
            print("\nContacto creado correctamente\n")
    else: print("Ese contacto ya existe") # valida para que no reescriba
    # reinicia la app despues de agregar o no
    app()

# --- U UPDATE / Editar contactos ---
def editar_contacto():
    nombre_anterior = input("Nombre del contacto que desea editar: \n")
    existe = existe_contacto(nombre_anterior) # la función existe_contacto() retornará True o False
    if existe: # si existe es True, ingresará al if
        with open(CARPETA + nombre_anterior + EXTENSION, "w", encoding="utf8") as archivo:
            # solicita los datos nuevos y los guarda en las variables
            nombre_contacto = input("Agrega el nuevo nombre: \n")
            telefono_contacto = input("Agrega el nuevo teléfono:\n")
            categoria_contacto = input("Agrega la nueva categoría:\n")

            # instancia la clase Contacto
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # escribe los cambios guardados en las variables en el archivo
            archivo.write (f"Nombre: {contacto.nombre}\n") # concatena y formatea el string con otro método diferente de agregar_contacto()
            archivo.write (f"Telefono: {contacto.telefono}\n")
            archivo.write (f"Categoria: {contacto.categoria}\n")

            # muestra mensaje de exito
            print("\nContacto modificado correctamente \n")

        # renombra el archivo si se cambió el nombre del contacto
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION) # metodo rename, primer argumento es el archivo existente y el segundo es el nombre nuevo del contacto
    else: # si la variable existe es False, imprime un aviso
        print("El contacto no existe")
    
    app()

def existe_contacto(nombre): # funcion que retornará un valor, utilizada en editar_contacto() para verificar si existe el contacto antes de editarlo
    return os.path.isfile(CARPETA + nombre + EXTENSION) # retorna True o False

# --- R READ / Mostrar contactos ---
def mostrar_contactos():
    # selecciona todos los archivos de la carpeta, como se haría con una base de datos, y los guarda en la variable archivos
    archivos = os.listdir(CARPETA) # almacena en archivos una lista con los nombres de los archivos del path CARPETA
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)] # valida que solamente los archivos que terminen con .txt sean utilizados, aquí se pondría la consulta SQL en caso de utilizar una base de datos
    print("--- Contactos ---\n")
    for archivo in archivos_txt: # recorre cada archivo validado como txt
        with open(CARPETA + archivo, encoding="utf8") as contacto:
            for i in contacto:
                print(i.rstrip()) # rstrip elimina los espacios en blanco
            print("\n") # separa cada contacto con un salto de linea

# --- Buscar contacto ---
def buscar_contacto():
    nombre = input("Seleccione el contacto que desea buscar: \n")
    # excepciones, para que el programa no caiga cuando se busca un contacto que no existe
    try: # intenta abrir el archivo con el nombre que ingresa el usuario
        with open(CARPETA + nombre + EXTENSION, encoding="utf8") as contacto:
            print("\nInformación del contacto: \n")
            for i in contacto: # con el mismo código que usa al editar, recorre la carpeta
                print(i.rstrip())
            print("\n")

    except IOError: # si el contacto no existe, mostrará un mensaje
        print("El contacto no existe\n")

    app()

# --- D DELETE / Eliminar contacto ---
def eliminar_contacto():
    nombre = input("Seleccione el contacto que desea eliminar: \n")
    try:
        os.remove(CARPETA + nombre + EXTENSION) # remove elimina un archivo con el nombre pasado como argumento
        print("\nEliminado correctamente\n")
    except:
        print("\nNo existe el contacto\n")

    app()

app()