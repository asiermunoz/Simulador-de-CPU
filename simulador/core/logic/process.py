from dataclasses import dataclass, field
from typing import Optional, List, Dict


@dataclass
class Process:
	"""Representación de un proceso para los algoritmos de planificación.

	Campos esenciales:
	- pid: identificador único (int)
	- arrival_time: instante de llegada (int)
	- burst_time: tiempo total de CPU requerido (int)
	- priority: prioridad (int), 0 por defecto (mayor valor = mayor prioridad depende del algoritmo)

	Campos calculados / de estado:
	- remaining_time: tiempo restante de CPU (int)
	- start_time: primer instante en que comenzó a ejecutarse (Optional[int])
	- completion_time: instante de terminación (Optional[int])
	- waiting_time: tiempo total de espera (int)
	- turn_around_time: tiempo de retorno (Optional[int])
	- response_time: tiempo de respuesta (Optional[int])
	- history: lista de segmentos ejecutados: dicts con keys (start, end)
	"""

	pid: int
	arrival_time: int
	burst_time: int
	priority: int = 0

	remaining_time: int = field(init=False)
	start_time: Optional[int] = None
	completion_time: Optional[int] = None
	waiting_time: int = 0
	turn_around_time: Optional[int] = None
	response_time: Optional[int] = None
	history: List[Dict[str, int]] = field(default_factory=list)

	def __post_init__(self):
		"""Valida los datos del proceso después de la inicialización."""
		if not isinstance(self.pid, int):
			raise TypeError("pid debe ser int")
		if self.arrival_time < 0:
			raise ValueError("arrival_time debe ser no negativo")
		if self.burst_time <= 0:
			raise ValueError("burst_time debe ser positivo (> 0)")
		self.remaining_time = int(self.burst_time)

	def is_finished(self) -> bool:
		return self.remaining_time <= 0

	def execute(self, time_slice: int, current_time: int) -> int:
		"""Ejecuta el proceso durante como máximo `time_slice` unidades a partir de `current_time`.

		Actualiza `start_time`, `response_time`, `remaining_time`, `completion_time`,
		`turn_around_time`, `waiting_time` y añade un segmento a `history`.

		Devuelve el tiempo realmente ejecutado (<= time_slice).
		"""
		if self.is_finished() or time_slice <= 0:
			return 0

		# Primer arranque
		if self.start_time is None:
			self.start_time = current_time
			self.response_time = self.start_time - self.arrival_time

		executed = min(self.remaining_time, int(time_slice))
		start_seg = current_time
		end_seg = current_time + executed
		self.history.append({"start": start_seg, "end": end_seg})

		self.remaining_time -= executed

		if self.remaining_time <= 0:
			self.completion_time = end_seg
			self.turn_around_time = self.completion_time - self.arrival_time
			self.waiting_time = self.turn_around_time - self.burst_time

		return executed

	def to_dict(self) -> Dict:
		return {
			"pid": self.pid,
			"arrival_time": self.arrival_time,
			"burst_time": self.burst_time,
			"remaining_time": self.remaining_time,
			"priority": self.priority,
			"start_time": self.start_time,
			"completion_time": self.completion_time,
			"waiting_time": self.waiting_time,
			"turn_around_time": self.turn_around_time,
			"response_time": self.response_time,
			"history": list(self.history),
		}

	@classmethod
	def from_dict(cls, data: Dict) -> "Process":
		p = cls(pid=int(data["pid"]), arrival_time=int(data["arrival_time"]), burst_time=int(data["burst_time"]), priority=int(data.get("priority", 0)))
		# allow injecting computed fields if present
		if "start_time" in data and data["start_time"] is not None:
			p.start_time = int(data["start_time"])
		if "completion_time" in data and data["completion_time"] is not None:
			p.completion_time = int(data["completion_time"])
		if "remaining_time" in data:
			p.remaining_time = int(data["remaining_time"])
		if "history" in data:
			p.history = list(data["history"])
		return p

	# Funciones de comparación útiles para ordenar listas de procesos
	def sort_key_arrival(self):
		return (self.arrival_time, self.pid)

	def sort_key_burst(self):
		return (self.burst_time, self.arrival_time, self.pid)

	def sort_key_remaining(self):
		return (self.remaining_time, self.arrival_time, self.pid)

	def sort_key_priority(self):
		return (self.priority, self.arrival_time, self.pid)

	def __repr__(self) -> str:
		return f"Process(pid={self.pid}, arrival={self.arrival_time}, burst={self.burst_time}, rem={self.remaining_time}, pri={self.priority})"

