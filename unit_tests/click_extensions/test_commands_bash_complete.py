import pytest

from click_extensions import commands, exit_codes


@pytest.mark.parametrize('app_name,bash_complete_name', [
    ('tigerhost', 'TIGERHOST'),
    ('tigerhost-deploy', 'TIGERHOST_DEPLOY'),
])
def test_bash_complete_name(app_name, bash_complete_name):
    assert commands._bash_complete_name(app_name) == bash_complete_name


def test_bash_complete_command(runner):
    result = runner.invoke(commands.bash_complete_command('test-app'))
    assert result.exit_code == exit_codes.SUCCESS
    assert '_TEST_APP_COMPLETE=source test-app' in result.output
