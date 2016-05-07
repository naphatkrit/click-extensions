import pytest

from click.testing import CliRunner


@pytest.yield_fixture(scope='function')
def runner():
    runner = CliRunner()
    with runner.isolated_filesystem():
        yield runner
