# Estructura de Contenedores y Componentes del Proyecto

generado por Gemini.com

```
simulador_cpu/
│
├── main.py                 # Punto de entrada (Responsabilidad de José - Full Stack)
├── requirements.txt        # Dependencias (matplotlib, etc.) [cite: 153]
│
├── core/                   # El corazón lógico (Responsabilidad de Asier - Ingeniero Algoritmos)
│   ├── __init__.py
│   ├── proceso.py          # Clase que define qué es un proceso (PCB)
│   ├── simulador.py        # Clase que orquesta la simulación
│   └── metricas.py         # Cálculos de espera, retorno, throughput
│
├── algoritmos/             # Implementación pura de los algoritmos [cite: 109, 110]
│   ├── __init__.py
│   ├── fcfs.py             # First-Come, First-Served
│   ├── sjf.py              # Shortest Job First
│   ├── round_robin.py      # Round Robin
│   └── prioridades.py      # Planificación por Prioridades
│
└── ui/                     # Interfaz Gráfica (Responsabilidad de José) [cite: 118]
    ├── __init__.py
    ├── ventana_principal.py
    └── gantt_plotter.py    # Generador de diagrama de Gantt usando Matplotlib

```