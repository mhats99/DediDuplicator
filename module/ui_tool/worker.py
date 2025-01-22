from concurrent.futures import ThreadPoolExecutor, as_completed
from PySide6.QtCore import QThread, Signal, QObject
from typing import Callable


class WorkerSignals(QObject):
    """Signals for the worker."""

    progress = Signal(int)
    finished = Signal(list)
    error = Signal(list)
    show_error = Signal(str)


class Worker(QThread):
    """
    Example usage:
    worker = Worker()

    worker.set_task(your_function, your_parameters)
    worker.start()

    """

    def __init__(self):

        super().__init__()
        self.function = None
        self.parameters = []
        self.executor = None  # Initialize executor as None
        self.is_running = False  
        self.signals = WorkerSignals()

    def set_task(self, function: Callable, parameters: list[list | tuple]):
        """Set the function and parameters for the worker."""

        if self.is_running:
            self.signals.show_error.emit("Worker running.")
            return

        self.function = function
        self.parameters = parameters

    def run(self):

        if self.function is None or not self.parameters:

            self.signals.show_error.emit("No function or parameters set.")
            self.cleanup()
            return

        else:

            self.is_running = True
            self.executor = ThreadPoolExecutor()  # Create the executor when running
            futures = {
                self.executor.submit(self.function, *param): param
                for param in self.parameters
            }

            result_list = []

            for i, future in enumerate(as_completed(futures)):
                param = futures[future]  # Get the parameters associated with the future
                try:
                    result_list.append(
                        future.result()
                    )  # This will raise an exception if the function failed
                    self.signals.progress.emit(i + 1)  # Emit progress signal
                except Exception as e:
                    self.signals.error.emit(f"{str(e)+"-"+str(param) }")  # Emit error signal

            self.cleanup()
            self.signals.finished.emit(result_list)  # Emit finished signal
            self.is_running = False

    def cleanup(self):
        """Clean up the executor when done."""

        if self.executor is not None:
            self.executor.shutdown(wait=True)
            self.executor = None  # Reset the executor
