# Exemplo de Dispatch Table vs match-case (Python moderno)

# Quando usar match? (match é um recurso que apareceu no Python 3.10)

# Conjunto fixo
# Não extensível
# Lógica pequena

# Quando usar Dispatch Table?

# Extensível
# Configurável
# Dinâmico
# Plugin-based
# Registrável em runtime

import typer
from typing import Callable

app = typer.Typer()

Operation = Callable[[int], int]
commands: dict[str, Operation] = {}


def register(name: str):
    def decorator(func: Operation) -> Operation:
        commands[name] = func
        return func
    return decorator


@register("double")
def double(x: int) -> int:
    return x * 2


@register("square")
def square(x: int) -> int:
    return x ** 2


@app.command()
def run(command: str, value: int):
    operation = commands.get(command)
    if operation is None:
        typer.echo("Unknown command")
        raise typer.Exit(code=1)

    typer.echo(operation(value))


if __name__ == "__main__":
    app()

# No código acima temos:

# Registro declarativo
# CLI extensível
# Arquitetura limpa
# Sem if/elif
# Sem herança artificial