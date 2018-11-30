import re
from unittest.mock import patch
from pydng.pydng import generate_name
from pydng.pydng import _fetch_latest_source
from pydng.pydng import _parse_source
from pydng.pydng import _random_docker_name


@patch('urllib.request.urlopen')
def test_generate_name(mocked_request):
    """
    Ensure we can generate a name in the expected format using
    a mocked request to get the source.
    """
    
    with open('tests/names-generator.go', 'rb') as go_source:
        source = go_source.read()

    mocked_request.return_value.read.return_value = source
    generated_name = generate_name()

    # Check if the "adjective_name" pattern is followed.
    assert re.match(r'\b[a-z]*_[a-z]*\b', generated_name)

    # Check if the adjective and name are valid in the source.
    assert generated_name.split("_")[0] in source.decode('utf-8')
    assert generated_name.split("_")[1] in source.decode('utf-8')


def test_fetch_latest_source():
    """ 
    Ensure the source
    1) Is what we're expecting (a string)
    2) Contains a few keywords we're expecting (aka it's the right thing)
    """
    source = _fetch_latest_source()

    assert type(source) == str
    assert "left" in source
    assert "right" in source
    assert "GetRandomName" in source


def test_parse_source():
    """ Ensure a tuple of two lists is returned """
    with open('tests/names-generator.go', 'r') as go_source:
        source = go_source.read()

    parsed_source = _parse_source(source)

    assert type(parsed_source) == tuple
    assert type(parsed_source[0]) == list
    assert type(parsed_source[1]) == list


def test_random_docker_name():
    """ Ensure it matches the Docker container name format """
    adjectives = ["derpy"]
    names = ["campbell"]
    generated_named = _random_docker_name(adjectives, names)
    assert generated_named == "derpy_campbell"
