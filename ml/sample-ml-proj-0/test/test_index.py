import pytest

from src import index


def test_main():
    assert index.main() == "Hello from sample-ml-proj-0!"
