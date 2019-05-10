"""The utils for the booty."""


def head(path, n=10, out=None):
    """Print the first n lines of a file.

    :param str path: The path to the file to print
    :param int n: The number of lines to print. Defaults to 10
    :param Optional[IO] out: An optional file to print to. If none, prints to stdout.
    """
    with open(path) as file:
        for number, line in zip(range(n), file):
            print(line.strip(), file=out)
