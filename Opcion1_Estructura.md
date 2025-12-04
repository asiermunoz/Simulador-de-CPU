# Estructura de Contenedores y Componentes del Proyecto

generado por Gemini.com

```
PROYECTO_SO/
│
├── venv/                   # Entorno virtual (Ignorar en Git)
├── manage.py               # Gestor de comandos
├── db.sqlite3              # Base de datos (Ignorar en Git si es posible)
│
├── config/                 # Configuración Global de Django
│   ├── settings.py         # ¡AQUÍ se registra la app 'simulador'!
│   └── urls.py             # Rutas principales
│
├── simulador/              # APP PRINCIPAL
│   ├── migrations/
│   ├── templates/          # FRONTEND (HTML)
│   │   └── simulador/
│   │       ├── base.html   # Estructura común (Navbar, Footer)
│   │       ├── index.html  # Formulario para meter procesos
│   │       └── resultado.html # Tabla y Gráfica de Gantt
│   │
│   ├── static/             # CSS / JS / Imágenes
│   │   └── css/
│   │       └── style.css
│   │
│   ├── views.py            # PUENTE: Recibe datos del HTML -> Llama a los algoritmos -> Devuelve resultados
│   ├── urls.py             # Rutas internas de la app
│   │
│   └── motor/              # ¡EL LABORATORIO DE ASIER! (Lógica pura)
│       ├── __init__.py
│       ├── proceso.py      # Clase Proceso (Objeto)
│       ├── fcfs.py         # Algoritmo First-Come First-Served
│       ├── sjf.py          # Algoritmo Shortest Job First
│       ├── prioridades.py  # Algoritmo por Prioridades
│       ├── rr.py           # Algoritmo Round Robin
│       └── monitor.py      # Clase que calcula promedios (WT, TAT)
```