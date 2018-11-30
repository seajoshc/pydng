import re
import pydng.pydng


def test_pydng():
    """ Ensure the generated name matches the proper format. """
    generated_name = pydng.generate_name()

    assert type(generated_name) == str
    assert re.match(r'\b[a-z]*_[a-z]*\b', generated_name)
