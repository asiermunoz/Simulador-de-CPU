from core.base.Logger import Logger
from core.base.Recorder import Recorder
from core.implementations.DefaultAlgorithm import DefaultAlgorithm





def main():
    """
    Docstring for main

    Los decoradores mejoran las capacidades de extender e integrar distintas funcionalidades
    en las implementaciones de los algoritmos sin modificar su codigo fuente.

    En este ejemplo, se decora DefaultAlgorithm con Logger y Recorder.
    1. Logger registra las llamadas y los datos yieldados por DefaultAlgorithm.
    2. Recorder procesa los datos yieldados (simulando grabacion o almacenamiento).

    Para mejorar la trazabilidad de los datos se puede tambien definir un tipo de dato
    para cada funcionalidad decoradora para identificar el origen de los datos y filtrar
    segun sea necesario.

    """
    proc = Recorder(Logger(DefaultAlgorithm()))
    # `Logger.execute` (and the decorated `execute` methods) are generators
    # (they use `yield`). Calling them without iterating will not run
    # their bodies. Consume the generator to execute the pipeline.
    result = list(proc.execute(param1="value1", param2="value2"))
    print("Final result:", *result)

if __name__ == "__main__":
    main()