from clint.textui import puts, indent, colored, prompt, validators
import click


@click.group()
@click.version_option()
def cli():
    """Extinct Gaming CLI Tools"""


@cli.group()
def backup():
    """Compress and Backup Files"""


@backup.command('local')
@click.argument('source')
@click.argument('dest')
def backup_local(source, dest):
    """Compress and Backup folder to Local Destination"""
    click.echo(click.style('Hello World!', fg='green'))
    click.secho('Backing up {} to {}'.format(source, dest), bg='blue', fg='white')

# from clint.textui import puts, indent, colored, prompt, validators

# puts('not indented text')
# with indent(4, quote=' ->'):
#     puts('indented text')
#     puts(colored.red('red text'))
#     puts(colored.blue('blue text'))
#     puts(colored.black('black text'))
#     puts(colored.cyan('cyan text'))
#     puts(colored.magenta('magenta text'))
#     puts(colored.green('green text'))
#     puts(colored.white('white text'))
#     puts(colored.yellow('yellow text'))
#     path = prompt.query('Installation Path', default='/usr/local/bin/', validators=[validators.PathValidator()])
