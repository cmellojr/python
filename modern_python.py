from typing import Callable, Iterable, Iterator, NewType, TextIO

# NewType: cria um tipo semântico
UserId = NewType("UserId", int)


# Iterator: produz dados sob demanda
def read_users(file: TextIO) -> Iterator[UserId]:
    for line in file:
        yield UserId(int(line.strip()))


# Iterable: algo que pode ser iterado (sem impor COMO)
def filter_even_users(users: Iterable[UserId]) -> Iterator[UserId]:
    for user in users:
        if user % 2 == 0:
            yield user


# Callable: comportamento injetável
def process_users(
    file: TextIO,
    processor: Callable[[Iterable[UserId]], int]
) -> int:
    users = read_users(file)
    filtered_users = filter_even_users(users)
    return processor(filtered_users)


# Um Callable concreto
def count_users(users: Iterable[UserId]) -> int:
    return sum(1 for _ in users)



