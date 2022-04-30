from expression import Expression, Environment
from pain_parser import Parser
import sys
from typing import Any


def run_file(fname: str, env: Environment) -> None:
    """
    >>> env = Environment({})
    >>> run_file("test-scripts/simple_arithmetic.pain", env)
    >>> env.get_value("test")
    11
    >>> env = Environment({})
    >>> run_file("test-scripts/more_complex_arithmetic.pain", env)
    >>> env.get_value("t")
    432
    """
    expressions: list[Expression] = []
    #filename = sys.argv[1]

    with open(fname) as f:
        contents = f.read()
        parser = Parser(contents)

        while True:
            expr = parser.parse_line()
            if expr is not None:
                expressions.append(expr)
            else:
                break

    for e in expressions:
        e.evaluate(env)


if __name__ == "__main__":
    import doctest
    doctest.testmod()