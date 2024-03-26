from typing import Any


class CustomDict:
    def __init__(self, table_size: int = 10) -> None:
        self._table_size: int = table_size  # Начальный размер хеш-таблицы
        self._data_dump: list[list[tuple[Any, Any]] | None] = [None] * self._table_size

    def __getitem__(self, key) -> Any | None:
        hash_key: int = self._hashing_key(key)
        if self._data_dump[hash_key] is None:
            # В ТЗ указано что нужно отдавать None - но это не совсем корректно,
            # ведь dict райзит KeyError
            raise KeyError("Key {key} not exists".format(key=key))

        for k, v in self._data_dump[hash_key]:
            if k == key:
                return v

        return None

    def __setitem__(self, key, value) -> None:
        hash_key = self._hashing_key(key)

        if self._data_dump[hash_key] is None:
            self._data_dump[hash_key] = []  # инициализируем ячейку

        for i, (k, v) in enumerate(self._data_dump[hash_key]):
            if k == key:
                self._data_dump[hash_key][i] = (key, value)
                return

        self._data_dump[hash_key].append((key, value))

    def __delitem__(self, key):
        hash_key = self._hashing_key(key)

        if self._data_dump[hash_key] is None:
            # Тут по-хорошему тоже бы райзить KeyError :)
            return

        for i, (k, v) in enumerate(self._data_dump[hash_key]):
            if k == key:
                del self._data_dump[hash_key][i]

                return

    def __str__(self) -> str:
        presented_data: str = ", ".join([f"{k}: {v}" for k, v in self.items()])

        return "{br_left}{pr_data}{br_right}".format(
            br_left="{", br_right="}", pr_data=presented_data
        )

    def _hashing_key(self, key: Any) -> int:
        return hash(key) % self._table_size

    def keys(self) -> list[Any]:
        keys: list[Any] = []

        for bucket in self._data_dump:
            if bucket:
                keys.extend([k for k, v in bucket])

        return keys

    def values(self) -> list[Any]:
        values: list[Any] = []

        for bucket in self._data_dump:
            if bucket:
                values.extend([v for k, v in bucket])

        return values

    def items(self) -> list[tuple[Any, Any]]:
        items: list[tuple[Any, Any]] = []

        for bucket in self._data_dump:
            if bucket:
                items.extend(bucket)

        return items
