import click

from functools import update_wrapper

import click_extensions

from click_extensions import exit_codes


def print_markers(f):
    """A decorator that prints the invoked command
    before and after the command.
    """
    @click.pass_context
    def new_func(ctx, *args, **kwargs):
        command = ctx.info_name
        assert command is not None
        command_name = ctx.command_path
        click_extensions.echo_with_markers(command_name, marker_color='green')

        def print_error(code):
            click_extensions.echo_with_markers('end of {} (exit code: {code})'.format(
                command_name, code=code), marker_color='red')

        def print_success():
            click_extensions.echo_with_markers('end of {}'.format(
                command_name), marker_color='green')
        try:
            ctx.invoke(f, *args, **kwargs)
        except SystemExit as e:
            code = e.code if e.code is not None else exit_codes.ABORT
            if code == 0:
                print_success()
            else:
                print_error(code)
            raise
        except click.ClickException as e:
            code = e.exit_code
            if code == 0:
                print_success()
            else:
                print_error(code)
            raise
        except click.Abort as e:
            code = exit_codes.ABORT
            print_error(code)
            raise
        except Exception as e:
            code = -1
            print_error(code)
            raise
        else:
            print_success()
            return
    return update_wrapper(new_func, f)


def catch_exception(exception, message=None):
    """A decorator that gracefully handles exceptions, exiting
    with :py:obj:`exit_codes.OTHER_FAILURE`.
    """
    def decorator(f):
        @click.pass_context
        def new_func(ctx, *args, **kwargs):
            try:
                return ctx.invoke(f, *args, **kwargs)
            except exception as e:
                message1 = message if message is not None else '{}'.format(e)
                click.echo(message1)
                ctx.exit(code=exit_codes.OTHER_FAILURE)
        return update_wrapper(new_func, f)
    return decorator


def ensure_obj(f):
    """A decorator that ensures context.obj exists. If it doesn't,
    a new dict() is created and stored as obj.
    """
    @click.pass_context
    def new_func(ctx, *args, **kwargs):
        if ctx.obj is None:
            ctx.obj = {}
        return ctx.invoke(f, *args, **kwargs)
    return update_wrapper(new_func, f)
