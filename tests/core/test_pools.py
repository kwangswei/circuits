# Module:   test_pools
# Date:     22nd February 2011
# Author:   James Mills, prologic at shortcircuit dot net dot au

"""Pools Tests"""

import pytest

from circuits import Task, Pool


def f():
    x = 0
    i = 0
    while i < 1000000:
        x += 1
        i += 1
    return x


def test_thread_pool():
    p = Pool()
    p.start()
    try:
        x = p.fire(Task(f))

        assert pytest.wait_for(x, "result")
        assert x.result
        assert x.value == 1000000

    finally:
        p.stop()


def test_process_pool():
    pytest.skip("XXX: Broken Functionality")
    p = Pool(process=True)
    p.start()
    try:
        x = p.fire(Task(f))

        assert pytest.wait_for(x, "result")
        assert x.result
        assert x.value == 1000000

    finally:
        p.stop()
