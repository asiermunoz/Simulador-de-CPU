from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_GET
from pathlib import Path
from django.http import JsonResponse

from main import AlgorithServiceSingleton
from core.implementations.DefaultAlgorithm import DefaultAlgorithm
from core.implementations.RoundRobin import RoundRobin
from core.implementations.ConcreteTimeRecorder import ConcreteTimeRecorder
from core.implementations.PollingLogger import PollingLogger
from core.base.Logger import Logger
from core.base.ProcessUpdateMonitor import ProcessUpdateMonitor
from core.base.Process import Process



@require_GET
def home(request):
    print(request.path)
    """Return the AlgorithmLogs.html static file from `views/AlgorithmLogs/`."""
    project_root = Path(__file__).resolve().parent.parent
    html_path = project_root / "views" / "AlgorithmLogs" / "AlgorithmLogs.html"

    if not html_path.exists():
        return HttpResponseNotFound("AlgorithmLogs.html not found")

    content = html_path.read_text(encoding="utf-8")
    return HttpResponse(content, content_type="text/html")


@require_GET
async def get_exec_data(request):
    instance = AlgorithServiceSingleton.getInstance()
    if instance is None:
        return JsonResponse({
            "name": "",
            "data": []
        })
    algorithm = instance.algorithm
    data = instance.pollLogs()
    return JsonResponse({
        "name": algorithm.getSignature(),
        "data": data
    })

@require_GET
def start_algorithm(request):
    algorithm = RoundRobin()
    instance = AlgorithServiceSingleton.getInstance(
        algorithm=
        PollingLogger(
            ProcessUpdateMonitor(
                ConcreteTimeRecorder(
                    algorithm
                    )
                )
            )
        )
    handle = instance.run(
        quantum=3,
        process_stack=Process.fromList([10, 5, 7, 9, 2])
    ) # Por ahora al terminar se reinicia.
    return JsonResponse({"status": instance.is_running()}, status=200)