#!/usr/bin/env python
"""
pydng
Docker Names Generator ported to Python
"""
from random import choice
import urllib.request


SOURCE_URL = "https://raw.githubusercontent.com/moby/moby/master/pkg/"\
             "namesgenerator/names-generator.go"


def main():
    """ main function """
    print(generate_name())


def generate_name():
    """
    Wrapper to fetch the latest source, parse it for adjectives and names,
    and then generating a random name in the Docker container style.

    Parameters
    ----------

    Returns
    -------
    str
        A name for a Docker container.
    """
    source = _fetch_latest_source()
    parsed = _parse_source(source)
    adjectives = parsed[0]
    names = parsed[1]
    names.append("rossum")  # ;)

    return _random_docker_name(adjectives, names)


def _fetch_latest_source():
    """
    Grabs the latest names-generator.go from moby/moby

    Parameters
    ----------

    Returns
    -------
    str
        The names-generator.go source code.
    """
    response = urllib.request.urlopen(SOURCE_URL)
    data = response.read()
    text = data.decode('utf-8')
    return text


def _parse_source(source):
    """
    Parses the names-generator.go source to find adjectives and names.

    Parameters
    ----------
    source : str
        The source file to be parsed.

    Returns
    -------
    tuple(2)
        Two lists with [0] being adjectives and [1] being names.
    """
    collecting = False
    left = []
    right = []
    side = ""

    for line in source.splitlines():
        # Immediately skip to the next line if this one is a comment.
        if "//" in line:
            continue
        # Lines immediately following either lines containing
        # "Left" or "Right" are of interest and we should start collecting.
        if "left" in line:
            collecting = True
            side = "left"
            continue
        if "right" in line:
            collecting = True
            side = "right"
            continue
        # Lines containing "}" mark when we should stop collecting.
        if "}" in line:
            collecting = False
            side = ""
            continue
        # We can stop the loop after this func declaration, we're done.
        if "func GetRandomName" in line:
            break
        # The adjectives and names we want to actually collect.
        if collecting and '"' in line:
            # Strip all whitespace, quotes, and commas.
            cleaned_line = line.strip().replace('"', "").replace(",", "")
            # Adjectives.
            if side == "left":
                left.append(cleaned_line)
            # Names.
            if side == "right":
                right.append(cleaned_line)
            continue

    return (left, right)


def _random_docker_name(adjectives, names):
    """
    Creates a random name for a Docker container based on two lists.

    Parameters
    ----------
    adjectives : list
        A list of adjectives (strings).

    names : list
        A list of names (strings).

    Returns
    -------
    string
        A name for a Docker container.
    """
    # Following the Docker container name format.
    return "{}_{}".format(choice(adjectives), choice(names))


if __name__ == "__main__":
    """ Your Favorite Wrappers' Favorite Wrapper """
    main()
