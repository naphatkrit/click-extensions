import click

import click_extensions

from click_extensions import exit_codes


def test_echo_with_marker(runner):
    heading = 'test heading'

    @click.command()
    def dummy():
        click_extensions.echo_with_markers(heading, marker='-')

    output = runner.invoke(dummy)
    assert output.exit_code == exit_codes.SUCCESS
    assert '- ' + heading + ' -' in output.output


def test_echo_heading(runner):
    heading = 'test heading'

    @click.command()
    def dummy():
        click_extensions.echo_heading(heading, marker='-')

    output = runner.invoke(dummy)
    assert output.exit_code == exit_codes.SUCCESS
    assert output.output == '---> ' + heading + '\n'
