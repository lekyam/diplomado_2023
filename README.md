# diplomado_2023

## El proyecto se encuentra deployado: [Aqui](https://flask-project-p2pp.onrender.com/)

## Pasos para levantar el proyecto en local windows

1. Ejecutar los siguientes comandos para descargar el proyecto y cambiar a la rama para la prueba local: 
~~~ 
git clone https://github.com/lekyam/diplomado_2023.git 
git checkout local-test
~~~
3. Crearemos la base de datos ejecutando los siguietes comandos (solo si lo requiere, debido a que la base esta ya deployada):
- Ejecutar:
  ~~~
  CREATE DATABASE diplomado;
  ~~~
- Ejecutar dentro la base de datos:
  ~~~
  CREATE TABLE public.usuario (
  cedula_identidad character varying NOT NULL,
  nombre character varying NOT NULL,
  primer_apellido character varying NOT NULL,
  segundo_apellido character varying NOT NULL,
  fecha_nacimiento date NOT NULL
  );
  ~~~
- Ejecutar dentro la base de datos:
  ~~~
  ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (cedula_identidad);
  ~~~
- Ejecutar dentro la base de datos:
  ~~~
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('1234567890', 'Juan', 'Pérez', 'Gómez', '1990-05-20');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('5678901234', 'Pedro', 'Ramírez', 'Sánchez', '1992-07-08');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('2345678901', 'Laura', 'Martínez', 'Hernández', '1988-12-03');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('8901234567', 'Carlos', 'López', 'Jiménez', '1995-03-25');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('3456789012', 'Ana', 'García', 'Rodríguez', '1997-11-17');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('0123456789', 'Luis', 'Díaz', 'Fernández', '1993-08-29');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('4567890123', 'Elena', 'Torres', 'Morales', '1994-06-14');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('7890123456', 'Javier', 'Soto', 'Vargas', '1991-02-10');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('6789012345', 'Sara', 'Ortega', 'Rojas', '1998-04-07');
  INSERT INTO public.usuario (cedula_identidad, nombre, primer_apellido, segundo_apellido, fecha_nacimiento) VALUES ('9359209', 'Maykel', 'Flores', 'Rodriguez', '2000-01-19');
  ~~~
3. Agregar el archivo **.env** en la raiz del proyecto, con este template (configuración de la base de datos ya deployada):
  ~~~
   PGSQL_HOST=dpg-chlde4rhp8uej74gilog-a.oregon-postgres.render.com
   PGSQL_USER=diplomado_user
   PGSQL_PASSWORD=HAAWrgiZfbHBho0tglXHpj8hGcIsTczO
   PGSQL_DATABASE=diplomado
   PGSQL_PORT=5432
  ~~~
4. Abrir la terminal y crear un entorno virtual para python para evitar que las dependencias se instalen de manera global
5. Crear venv con el comando: 
~~~
python -m virtualenv venv
~~~
6. Activar el entorno virtual con el comando: 
~~~
.\venv\Scripts\activate
~~~
7. Instalar las dependencias (Asegurarse de estar en el entorno virtual y en el directorio del archivo) con el comando:
~~~
pip install -r requirement.txt
~~~
8. Y finalizar ejecutando el comando: 
~~~
python src\app.py
~~~ 
9. si todo sale bien se ejecutaria en el puerto http://127.0.0.1:5000

## Documentación API

La documentación la hice con la libreria flask_restx que implementa Swagger UI que implementaria la documentación del proyecto

## Dependecias utilizadas

- flask
- flask-cors
- psycopg2
- python-decouple
- python-dotenv
- python-dateutil
- flask_restx
- gunicorn
