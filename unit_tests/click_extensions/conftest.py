import mock
import os
import pytest

from temp_utils.contextmanagers import temp_dir

from click.testing import CliRunner


@pytest.yield_fixture(scope='function')
def runner():
    runner = CliRunner()
    with runner.isolated_filesystem():
        yield runner


@pytest.yield_fixture(scope='function', autouse=True)
def fake_private_dir():
    with temp_dir() as path:
        new_private_dir = os.path.join(path, '.app-name')
        with mock.patch('click_extensions.private_dir.private_dir_path') as mocked:
            mocked.return_value = new_private_dir
            yield
