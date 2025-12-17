from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_GET
from pathlib import Path

from main import AlgorithServiceSingleton
from core.implementations.DefaultAlgorithm import DefaultAlgorithm
from core.implementations.ConcreteTimeRecorder import ConcreteTimeRecorder
from core.implementations.PollingLogger import PollingLogger
from core.base.Logger import Logger



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
    instance = AlgorithServiceSingleton.getInstance(algorithm=PollingLogger(ConcreteTimeRecorder(DefaultAlgorithm())))
    handle = instance.run()
    data = instance.pollLogs()
    from django.http import JsonResponse
    return JsonResponse({
        "name": "DefaultAlgorithm",
        "data": data
        })