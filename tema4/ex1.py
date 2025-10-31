from typing import Generic, Iterable, List, Optional, TypeVar

T = TypeVar("T")

class Stack(Generic[T]):
	def __init__(self, items: Optional[Iterable[T]] = None) -> None:
		self._data: List[T] = []
		if items is not None:
			self._data.extend(items)

	def push(self, item: T) -> None:
		self._data.append(item)

	def pop(self) -> Optional[T]:
		if not self._data:
			return None
		return self._data.pop()

	def peek(self) -> Optional[T]:
		if not self._data:
			return None
		return self._data[-1]

	def is_empty(self) -> bool:
		return not self._data

	def size(self) -> int:
		return len(self._data)

	def __len__(self) -> int:
		return len(self._data)

	def __bool__(self) -> bool:
		return bool(self._data)

	def __repr__(self) -> str:
		return f"Stack({self._data!r})"


s: Stack[int] = Stack()
print("peek on empty:", s.peek())
print("pop on empty:", s.pop())
s.push(10)
s.push(20)
print("peek:", s.peek())
print("pop:", s.pop())
print("peek after pop:", s.peek())
print("size:", s.size())