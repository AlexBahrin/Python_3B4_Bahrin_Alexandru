from typing import Callable, Generic, Iterable, List, Sequence, Tuple, TypeVar, Union

T = TypeVar("T")
U = TypeVar("U")


class Matrix(Generic[T]):
	def __init__(self, n: int, m: int, fill: Union[T, int, float] = 0) -> None:
		if n <= 0 or m <= 0:
			raise ValueError("Matrix dimensions must be positive")
		self.n = int(n)
		self.m = int(m)
		self._a: List[List[T]] = [[fill for _ in range(self.m)] for _ in range(self.n)]

	def _check_bounds(self, i: int, j: int) -> None:
		if not (0 <= i < self.n and 0 <= j < self.m):
			raise IndexError(f"Index out of bounds: ({i}, {j}) for shape ({self.n}, {self.m})")

	def get(self, i: int, j: int) -> T:
		self._check_bounds(i, j)
		return self._a[i][j]

	def set(self, i: int, j: int, value: T) -> None:
		self._check_bounds(i, j)
		self._a[i][j] = value

	def __getitem__(self, key: Tuple[int, int]) -> T:
		i, j = key
		return self.get(i, j)

	def __setitem__(self, key: Tuple[int, int], value: T) -> None:
		i, j = key
		self.set(i, j, value)

	def map(self, func: Callable[[T], U]) -> "Matrix[U]":
		out: Matrix[U] = Matrix(self.n, self.m)
		for i in range(self.n):
			for j in range(self.m):
				out._a[i][j] = func(self._a[i][j])
		return out

	def transpose(self) -> "Matrix[T]":
		t = Matrix(self.m, self.n)
		for i in range(self.n):
			for j in range(self.m):
				t._a[j][i] = self._a[i][j]
		return t

	def matmul(self, other: "Matrix") -> "Matrix":
		if self.m != other.n:
			raise ValueError(
				f"Incompatible shapes for matmul: ({self.n}, {self.m}) x ({other.n}, {other.m})"
			)
		result = Matrix(self.n, other.m, fill=0)
		for i in range(self.n):
			row_i = self._a[i]
			for k in range(self.m):
				a_ik = row_i[k]
				if a_ik == 0:
					continue
				col_k = other._a[k]
				for j in range(other.m):
					result._a[i][j] += a_ik * col_k[j]
		return result

	def __matmul__(self, other: "Matrix") -> "Matrix":
		return self.matmul(other)

	def __repr__(self) -> str:
		return f"Matrix(n={self.n}, m={self.m}, data={self._a!r})"

	def __str__(self) -> str:
		return "\n".join("[" + ", ".join(str(x) for x in row) + "]" for row in self._a)

	def __eq__(self, other: object) -> bool:
		if not isinstance(other, Matrix):
			return False
		return self.n == other.n and self.m == other.m and self._a == other._a

	@classmethod
	def from_rows(cls, rows: Sequence[Sequence[T]]) -> "Matrix[T]":
		if not rows:
			raise ValueError("rows must be a non-empty 2D sequence")
		n = len(rows)
		m = len(rows[0])
		if any(len(r) != m for r in rows):
			raise ValueError("All rows must have the same length")
		mat = cls(n, m)
		for i in range(n):
			for j in range(m):
				mat._a[i][j] = rows[i][j]
		return mat


A = Matrix.from_rows([[1, 2, 3], [4, 5, 6]])
print("A:")
print(A)

print("A[0, 1] =", A.get(0, 1))
A.set(0, 1, 20)
print("After set(0,1,20):")
print(A)

AT = A.transpose()
print("A^T:")
print(AT)

B = Matrix.from_rows([[1, 0], [0, 1], [1, 1]])
print("B:")
print(B)
C = A @ B
print("C = A @ B:")
print(C)

D = C.map(lambda x: x + 1)
print("D = C.map(lambda x: x + 1):")
print(D)

