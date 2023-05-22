# diplomado_2023

## Database Queries

Yo trabaje con un entorno virtual

## Pasos para levantar el proyecto

1. Descargar el proyecto
2. Crearemos la base de datos ejecutando los siguietes comandos:

## comandos para crear la base de datos

- CREATE DATABASE diplomado;

### dentro de la base de datos creada ejecutamos los siguientes comandos

- CREATE TABLE public.usuario (
  cedula_identidad character varying NOT NULL,
  nombre character varying NOT NULL,
  primer_apellido character varying NOT NULL,
  segundo_apellido character varying NOT NULL,
  fecha_nacimiento date NOT NULL
  );

- ALTER TABLE ONLY public.usuario
  ADD CONSTRAINT usuario_pkey PRIMARY KEY (cedula_identidad);

- INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('1234567890', 'Juan', 'Pérez', 'Gómez', '1990-05-20');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('5678901234', 'Pedro', 'Ramírez', 'Sánchez', '1992-07-08');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('2345678901', 'Laura', 'Martínez', 'Hernández', '1988-12-03');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('8901234567', 'Carlos', 'López', 'Jiménez', '1995-03-25');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('3456789012', 'Ana', 'García', 'Rodríguez', '1997-11-17');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('0123456789', 'Luis', 'Díaz', 'Fernández', '1993-08-29');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('4567890123', 'Elena', 'Torres', 'Morales', '1994-06-14');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('7890123456', 'Javier', 'Soto', 'Vargas', '1991-02-10');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('6789012345', 'Sara', 'Ortega', 'Rojas', '1998-04-07');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('9359209', 'Maykel', 'Flores', 'Rodriguez', '2000-01-19');

3. Agregar el archivo ".env" en la raiz del proyecto, con este template:
   SECRET_KEY=FLASKPASS
   PGSQL_HOST=your_localhost
   PGSQL_USER=your_user
   PGSQL_PASSWORD=your_password
   PGSQL_DATABASE=diplomado
   PGSQL_PORT=your_port

4. Actualizar en el archivo ".env" los nuevos datos para la conexion con postgres
5. Abrir la terminal y crear un entorno virtual para python para evitar que las dependencias se instalen de manera global
6. Crear venv con el comando: python -m virtualenv venv
7. Activar el entorno virtual con el comando: .\venv\Scripts\activate
8. Instalar las dependencias (Asegurarse de estar en el entorno virtual) con el comando: pip install -r requirement.txt asegurarse de estar en el directorio del archivo
9. Y finalizar ejecutando el comando: python src\app.py si todo sale bien se ejecutaria en el puerto http://127.0.0.1:5000

## Documentación API

La documentación la hice con la libreria flask_restx que implementa Swagger UI que implementaria la documentación del proyecto

## Dependecias usadas

- flask
- flask-cors
- psycopg2
- python-decouple
- python-dotenv
- python-dateutil
- flask_restx
