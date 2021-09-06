# CRUD Contactos del teléfono

[![Gitter](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)](https://www.python.org/)

## Descripción

Esta aplicación simula el manejo de contactos en un teléfono usando el lenguaje Python, creando contactos nuevos, mostrándolos, modificándolos y eliminándolos cuando se necesite.

## Tecnologías

[Python](https://www.python.org/) es un lenguaje de programación potente y fácil de aprender. Tiene estructuras de datos de alto nivel eficientes y un simple pero efectivo sistema de programación orientado a objetos. La elegante sintaxis de Python y su tipado dinámico, junto a su naturaleza interpretada lo convierten en un lenguaje ideal para scripting y desarrollo rápido de aplicaciones en muchas áreas, para la mayoría de plataformas.

## Instalación

No es necesario instalar ningún paquete externo, el módulo os se importa automáticamente en el archivo.

## Uso

El programa muestra un menú donde el usuario elige con un número que opción quiere realizar.

Para agregar un nuevo contacto se elige el número 1 y se determina el nombre, número y categoría del contacto, que se guardará como texto plano en la carpeta Contactos, la cual se creará si no existe:

![1- Agregar](img/agregar.jpg)

Para editar el contacto, el programa pedirá un nombre de contacto y lo buscará en la carpeta, si el contacto existe pedirá el nuevo nombre, teléfono y categoría:

![2- Editar](img/editar.jpg)

La opción de ver contactos mostrará todos los contactos que el usuario tiene guardados hasta el momento:

![3- Ver](img/ver.jpg)

La opción buscar pedirá el nombre del contacto que se desea mostrar e imprimirá su información:

![4- Buscar](img/buscar.jpg)

A su vez, la opción eliminar pedirá el nombre del contacto que se quiere eliminar y lo hará, en este caso el contacto no existía:

![5- Eliminar](img/eliminar.jpg)

Por último, la opción 6 permite salir del programa.

## Soporte

Si necesitas soporte sobre el programa, podes [comunicarte](paola.cartala@gmail.com "Enviame un mail!") conmigo.

## Roadmap

Las ideas que tengo para futuras versiones son:

- Agregar confirmación de eliminación de contacto

## Contribuciones

Este repositorio está abierto a contribuciones, no dudes en hacerlo!

## Autores y agradecimientos

Este código fue originalmente escrito por Juan Pablo De la torre Valdez de https://codigoconjuan.com/ a través de [Udemy](https://www.udemy.com/), el cual modifiqué ligeramente.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
