# CRUD de Proveedores con Flask y PostgreSQL

Proyecto desarrollado para el curso de Desarrollo Web de la Universidad Mariano Gálvez.

## Descripción

Aplicación web para la gestión de proveedores utilizando Flask y PostgreSQL. El sistema permite registrar, consultar, editar y eliminar proveedores mediante una interfaz desarrollada con Bootstrap y estilos personalizados.

## Funcionalidades

- Registrar nuevos proveedores.
- Listar proveedores registrados.
- Editar información de proveedores.
- Eliminar proveedores.
- Manejar proveedores activos e inactivos.
- Validar los datos ingresados en los formularios.
- Almacenar la información en PostgreSQL.

## Tecnologías utilizadas

- Python
- Flask
- PostgreSQL
- HTML5
- CSS3
- Bootstrap
- Jinja2

## Base de datos

La aplicación utiliza una base de datos PostgreSQL llamada `proveedores_db`.

La tabla principal almacena:

- Nombre
- NIT
- Teléfono
- Correo electrónico
- Dirección
- Estado
- Fecha de registro

## Seguridad

Las credenciales de conexión se almacenan mediante variables de entorno en un archivo `.env`.

El archivo `.env` está excluido del repositorio mediante `.gitignore` para evitar publicar información privada.