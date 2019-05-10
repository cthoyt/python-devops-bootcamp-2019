"""
To run this file from the command line, call it as a module using:

python -m booty.cli
"""

import click

from booty.utils import head


@click.command(help='This CLI runs the booty')
@click.argument('path')
@click.option('-n', '--number-lines', default=10, type=int)
def main(path, number_lines):
    head(path, n=number_lines)


if __name__ == '__main__':
    main()
