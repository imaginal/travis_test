import sys
import asyncio
from unittest.mock import patch
from dozorro.api.main import cdb_init


def test_main():
    assert True


def test_cdb_init():
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    testargs = ["cdb_init", "--dropdb", "tests/keyring/root.json"]
    with patch.object(sys, 'argv', testargs):
        cdb_init()
