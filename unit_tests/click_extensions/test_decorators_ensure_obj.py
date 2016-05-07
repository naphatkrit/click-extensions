import click
import pytest

from click_extensions import decorators


@click.command()
@click.pass_context
@decorators.ensure_obj
def ensure_once(ctx):
    assert ctx.obj == {}


@click.command()
@click.pass_context
@decorators.ensure_obj
@decorators.ensure_obj
def ensure_twice(ctx):
    assert ctx.obj == {}


@pytest.mark.parametrize('command,exit_code', [
    (ensure_once, 0),
    (ensure_twice, 0),
])
def test_simple(runner, command, exit_code):
    result = runner.invoke(command)
    assert result.exit_code == exit_code
