from twttr import shorten
import random


def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("z4nd3r") == "z4nd3r"
    assert shorten("avery.") == "vry."
