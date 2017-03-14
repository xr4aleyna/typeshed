from typing import TypeVar, Generic, Any, Iterable, Iterator, Callable, Optional, Set, Tuple, Union

_T = TypeVar('_T')

class Error(Exception): ...
class CancelledError(Error): ...
class TimeoutError(Error): ...

class Future(Generic[_T]):
    def cancel(self) -> bool: ...
    def cancelled(self) -> bool: ...
    def running(self) -> bool: ...
    def done(self) -> bool: ...
    def result(self, timeout: float = ...) -> _T: ...
    def exception(self, timeout: float = ...) -> Any: ...
    def add_done_callback(self, fn: Callable[[Future], Any]) -> None: ...

    def set_running_or_notify_cancel(self) -> None: ...
    def set_result(self, result: _T) -> None: ...
    def set_exception(self, exception: Any) -> None: ...

class Executor:
    def submit(self, fn: Callable[..., _T], *args: Any, **kwargs: Any) -> Future[_T]: ...
    def map(self, func: Callable[..., _T], *iterables: Any, timeout: float = ...) -> Iterable[_T]: ...
    def shutdown(self, wait: bool = ...) -> None: ...
    def __enter__(self) -> Executor: ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool: ...

class ThreadPoolExecutor(Executor):
    def __init__(self, max_workers: int) -> None: ...

class ProcessPoolExecutor(Executor):
    def __init__(self, max_workers: Union[int, None] = ...) -> None: ...

def wait(fs: Iterable[Future], timeout: Optional[float] = ..., return_when: str = ...) -> Tuple[Set[Future], Set[Future]]: ...

FIRST_COMPLETED = ...  # type: str
FIRST_EXCEPTION = ...  # type: str
ALL_COMPLETED = ...  # type: str

def as_completed(fs: Iterable[Future], timeout: float = ...) -> Iterator[Future]: ...
