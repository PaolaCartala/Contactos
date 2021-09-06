import os

# -- Valores que se usarán constantemente --
CARPETA = "Contactos/"
EXTENSION = ".txt"

# --- Clase Contacto ---
class Contacto:
    """
    Clase que contendrá los atributos que se guardarán en los contactos
    """
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

# --- Función principal que contendrá todas las opciones ---
def app():
    """
    Contiene las funciones que muestran el menú principal y crean la carpeta y los archivos con los contactos
    """
    crear_directorio()
    mostrar_menu()

    # --- Elección de opciones por parte del usuario ---
    preguntar = True
    while preguntar:
        opcion = int(input("Seleccione una opción: \n")) 
        if opcion == 1:
            agregar_contacto()
            preguntar = False
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
            preguntar = False
        else:
            print("Opción no válida, intente de nuevo")

# --- Crea el directorio donde se guardarán los contactos ---
def crear_directorio():
    """
    Verifica si la carpeta Contactos fue creada anteriormente, sino la crea.
    """
    if not os.path.exists(CARPETA):
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
    """
    Pide los datos que queremos guardar en el contacto, valida si el archivo existe antes de crearlo, si no existe lo crea y escribe los datos instanciados de la clase Contacto, luego muestra un mensaje de éxito. Si el contacto ya existía también muestra un mensaje de aviso.
    """
    print("Escribe los datos para agregar el nuevo contacto:")
    nombre_contacto = input("Nombre del Contacto:\n").capitalize()
    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION)
    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, "w", encoding="utf8") as archivo:
            telefono_contacto = int(input("Agrega el teléfono del contacto:\n"))
            categoria_contacto = input("Agrega la categoría del contacto:\n").capitalize()

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
            
            archivo.write ("Nombre: " + contacto.nombre + "\n")
            archivo.write ("Telefono: " + str(contacto.telefono) + "\n")
            archivo.write ("Categoria: " + contacto.categoria + "\n")

            print("\nContacto creado correctamente\n")
    else: print("Ese contacto ya existe")
    app()

# --- U UPDATE / Editar contactos ---
def editar_contacto():
    """
    Verifica si el contacto existe y lo edita instanciando nuevamente la Clase Contacto, luego cambia el nombre del archivo. Si no existe, muestra un mensaje de aviso.
    """
    nombre_anterior = input("Nombre del contacto que desea editar: \n")
    existe = existe_contacto(nombre_anterior)
    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, "w", encoding="utf8") as archivo:
            nombre_contacto = input("Agrega el nuevo nombre: \n")
            telefono_contacto = input("Agrega el nuevo teléfono:\n")
            categoria_contacto = input("Agrega la nueva categoría:\n")

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write (f"Nombre: {contacto.nombre}\n")
            archivo.write (f"Telefono: {contacto.telefono}\n")
            archivo.write (f"Categoria: {contacto.categoria}\n")

            print("\nContacto modificado correctamente \n")

        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
    else:
        print("El contacto no existe")
    
    app()

def existe_contacto(nombre):
    """
    Verifica si el archivo con el nombre de contacto existe en la carpeta.
    """
    return os.path.isfile(CARPETA + nombre + EXTENSION)

# --- R READ / Mostrar contactos ---
def mostrar_contactos():
    """
    Selecciona todos los archivos de la carpeta, como se haría con una base de datos, y los guarda en la variable archivos, luego recorre cada archivo validado como .txt y lo muestra.
    """
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    print("--- Contactos ---\n")
    for archivo in archivos_txt:
        with open(CARPETA + archivo, encoding="utf8") as contacto:
            for i in contacto:
                print(i.rstrip())
            print("\n")

# --- Buscar contacto ---
def buscar_contacto():
    """
    Utiliza el manejo de excepciones para buscar un archivo con determinado nombre en la carpeta Contactos, si el archivo existe muestra su contenido, si no muestra un mensaje.
    """
    nombre = input("Seleccione el contacto que desea buscar: \n")
    try:
        with open(CARPETA + nombre + EXTENSION, encoding="utf8") as contacto:
            print("\nInformación del contacto: \n")
            for i in contacto:
                print(i.rstrip())
            print("\n")

    except IOError:
        print("El contacto no existe\n")

    app()

# --- D DELETE / Eliminar contacto ---
def eliminar_contacto():
    """
    Intenta buscar el contacto que ingresa el usuario y si existe lo elimina, si no muestra un mensaje.
    """
    nombre = input("Seleccione el contacto que desea eliminar: \n")
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print("\nEliminado correctamente\n")
    except:
        print("\nNo existe el contacto\n")

    app()

app()