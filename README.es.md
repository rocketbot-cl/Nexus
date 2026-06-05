



# Nexus
  
Módulo para conectarse a la API de Nexus, permitiendo leer/escribir datos y escuchar eventos en tiempo real.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Overview


1. Conectar a Nexus  
Establece una sesión con la API de Nexus usando una API Key.

2. Listar Tablas  
Retorna todas las tablas disponibles para esta API Key.

3. Obtener Tabla  
Retorna la definición de una tabla por su ID.

4. Crear Tabla  
Crea una nueva tabla.

5. Actualizar Tabla  
Actualiza metadatos de la tabla (nombre, columnas).

6. Eliminar Tabla  
Elimina permanentemente una tabla y todas sus filas.

7. Actualizar Celda  
Actualiza el valor de una celda en una fila.

8. Obtener Filas  
Obtiene filas de una tabla de Nexus.

9. Insertar Fila  
Inserta una nueva fila en una tabla de Nexus.

10. Actualizar Fila  
Actualiza una fila existente por su ID.

11. Eliminar Fila  
Elimina una fila por su ID.

12. Eliminar Todas las Filas  
Borra todas las filas de una tabla sin eliminar la tabla.

13. Listar Consultas  
Retorna todas las consultas guardadas para esta API Key.

14. Ejecutar Query  
Ejecuta una query guardada en Nexus con parámetros opcionales.  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**requests**](https://pypi.org/project/requests/)
### License
  
![MIT](https://img.shields.io/github/license/instaloader/instaloader.svg)  
[MIT](https://opensource.org/license/mit)