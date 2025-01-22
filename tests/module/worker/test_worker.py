import pytest
from module.ui_tool import Worker


@pytest.fixture
def worker():
    return Worker()


def dummy_function(x):
    if x < 0:
        raise ValueError("Negative value!")
    return x * 2


def test_set_task(worker):
    worker.set_task(dummy_function, [(1,), (2,)])
    assert worker.function is dummy_function
    assert worker.parameters == [(1,), (2,)]


def test_set_task_while_running(worker):
    worker.is_running = True
    worker.set_task(dummy_function, [(1,)])
    assert worker.function is None
    assert worker.parameters == []


def test_run_no_task(worker, qtbot):
    with qtbot.waitSignal(worker.signals.show_error, timeout=1000) as blocker:
        worker.run()
    assert blocker.args == ["No function or parameters set."]


def test_run_success(worker, qtbot):
    worker.set_task(dummy_function, [(1,), (2,)])
    with qtbot.waitSignal(worker.signals.finished, timeout=5000) as blocker:
        worker.start()
    assert blocker.args == [[2, 4]]


def test_run_error(worker, qtbot):
    worker.set_task(dummy_function, [(1,), (-1,)])
    with qtbot.waitSignal(worker.signals.error, timeout=5000) as blocker:
        worker.start()
    assert "".join(blocker.args[0]) == "Negative value!-(-1,)"


def test_run_mixed(worker, qtbot):
    worker.set_task(dummy_function, [(1,), (-1,), (3,)])
    progress_signals_received = 0
    finished_signal_received = False
    error_signal_received = False

    def progress_callback(value):
        nonlocal progress_signals_received
        progress_signals_received += 1
        print(
            f"Progress signal {progress_signals_received} received with value: {value}"
        )

    def finished_callback(result):
        nonlocal finished_signal_received
        finished_signal_received = True
        print(f"Finished signal received with result: {result}")
        assert result == [2, 6]

    def error_callback(error):
        nonlocal error_signal_received
        error_signal_received = True
        print(f"Error signal received with error: {error}")

    worker.signals.progress.connect(progress_callback)
    worker.signals.finished.connect(finished_callback)
    worker.signals.error.connect(error_callback)

    worker.start()

    qtbot.wait_until(
        lambda: finished_signal_received or error_signal_received, timeout=10000
    )

    assert (
        progress_signals_received == 2
    ), f"Expected 2 progress signals, got {progress_signals_received}"
    assert finished_signal_received, "Finished signal not received"
    assert error_signal_received, "Error signal not received for the negative value"


def test_cleanup(worker):
    worker.set_task(dummy_function, [(1,), (2,)])
    worker.run()
    worker.cleanup()
    assert worker.executor is None


if __name__ == "__main__":
    pytest.main()
