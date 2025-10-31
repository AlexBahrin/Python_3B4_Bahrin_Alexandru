from collections import deque
from typing import Deque, Generic, Iterable, Optional, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
	def __init__(self, iterable: Optional[Iterable[T]] = None) -> None:
		self._data: Deque[T] = deque()
		if iterable is not None:
			for item in iterable:
				self.push(item)

	def push(self, item: T) -> None:
		self._data.append(item)

	def pop(self) -> Optional[T]:
		if not self._data:
			return None
		return self._data.popleft()

	def peek(self) -> Optional[T]:
		if not self._data:
			return None
		return self._data[0]

	def __len__(self) -> int:
		return len(self._data)

	def is_empty(self) -> bool:
		return not self._data

	def __repr__(self) -> str:
		return f"Queue({list(self._data)!r})"

q: Queue[int] = Queue()
print(q.peek())
print(q.pop())

q.push(1)
q.push(2)
q.push(3)

print(q.peek())
print(q.pop())
print(q.pop())
print(len(q))
print(q.is_empty())
print(q.pop())
print(q.is_empty())