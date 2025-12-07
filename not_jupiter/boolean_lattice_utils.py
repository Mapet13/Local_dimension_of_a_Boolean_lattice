from itertools import count, islice, filterfalse
from typing import Generator, Iterable

type Ple = list[int]
type Realizer = list[Ple]
type Elements_generator = Generator[int, None, None]
type Elements_iterator = Iterable[int]


def singletons_gen() -> Elements_generator:
    for i in count():
        yield (1 << i)


def elements_gen(n: int) -> Elements_iterator:
    return range(1 << n)


def is_singleton(x: int):
    return x.bit_count() == 1


def is_pair(x: int):
    return x.bit_count() == 2


def count_elements(x: int):
    return x.bit_count()


def not_singletons_gen(n: int) -> Elements_iterator:
    return filterfalse(is_singleton, elements_gen(n))


def pairs_gen(n: int) -> Elements_iterator:
    return filter(is_pair, elements_gen(n))


def singletons_gen_n(n: int) -> Elements_iterator:
    return islice(singletons_gen(), n)


def is_subset(a: int, b: int) -> bool:
    return (a | b) == b


def to_string(
    a: int,
    n: int,
    with_gaps: bool = False,
    should_center=True,
    mapper: callable = lambda x: x,
) -> str:
    if a == 0:
        return "(/)".center(n)

    pows = list(map(mapper, [1 << i for i in range(n)]))

    s = ""
    for i in range(n):
        if a & pows[i] != 0:
            s += str(i + 1)
        elif with_gaps:
            s += " "
    return s if with_gaps or not should_center else s.center(n)
