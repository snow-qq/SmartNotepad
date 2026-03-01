import time


class PerformanceMonitor:
    def measure(self, name: str):
        return _Timer(name)


class _Timer:
    def __init__(self, name: str) -> None:
        self.name = name
        self._start = 0.0

    def __enter__(self):
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        elapsed = (time.perf_counter() - self._start) * 1000
        print(f"{self.name}: {elapsed:.2f} ms")