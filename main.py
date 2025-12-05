from core.base.Logger import Logger
from core.base.Recorder import Recorder
from core.implementations.DefaultAlgorithm import DefaultAlgorithm





def main():
    proc = Recorder(Logger(DefaultAlgorithm()))
    # `Logger.execute` (and the decorated `execute` methods) are generators
    # (they use `yield`). Calling them without iterating will not run
    # their bodies. Consume the generator to execute the pipeline.
    result = list(proc.execute(param1="value1", param2="value2"))
    print("Final result:", *result)

if __name__ == "__main__":
    main()