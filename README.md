# Simulador-de-CPU
En este repositorio se encuentra el proyecto de Sistemas Operativos, un simulador de algoritmos de planificación de la CPU, en Python 3.14, usando Django como framework para la interfaz web

## Pasos realizados para iniciar el proyecto e instalar Django (zsh)
- Crear entorno virtual:
	```zsh
	python3 -m venv .venv
	```
- Activar entorno virtual:
	```zsh
	source .venv/bin/activate
	```
- Actualizar `pip` y herramientas básicas:
	```zsh
	python -m pip install --upgrade pip wheel setuptools
	```
- Instalar Django:
	```zsh
	pip install django
	```
- Verificar versión de Django instalada:
	```zsh
	python -m django --version
	```
- Crear el proyecto Django en el directorio actual (estructura `config/` ya presente):
	```zsh
	django-admin startproject config .
	```
- Aplicar migraciones iniciales:
	```zsh
	python manage.py migrate
	```
- Ejecutar el servidor de desarrollo para validar la instalación:
	```zsh
	python manage.py runserver
	```
- (Opcional) Crear una aplicación dentro del proyecto:
	```zsh
	python manage.py startapp simulador
	```
- (Opcional) Guardar dependencias en `requirements.txt`:
	```zsh
	pip freeze > requirements.txt
	```

Notas:
- Estas instrucciones reflejan los pasos estándar realizados para iniciar un proyecto Django y coinciden con la estructura actual del repositorio (`manage.py` y carpeta `config/`).
- Si ya existía la carpeta `config/`, el comando `startproject` puede haberse omitido; en tal caso, mantén los pasos de instalación y ejecución.


