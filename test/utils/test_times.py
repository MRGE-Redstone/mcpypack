import pytest

from MCpypack.utils import (
    Time,
    Milliseconds,
    Seconds,
    Minutes,
    Hours,
)

def test_single_milliseconds():
    t = Time(Milliseconds(1500))

    assert t.milliseconds.value == 1500
    assert t.seconds.value == 0
    assert t.ticks.value == 30 # 1500ms -> 30 ticks

def test_single_seconds():
    t = Time(Seconds(2))
    assert t.seconds.value == 2
    assert t.ticks.value == 40  # 2s -> 40 ticks

def test_mixed_time_units():
    t = Time(
        Milliseconds(500),
        Seconds(10),
        Minutes(1),
        Hours(1),
    )

    assert t.milliseconds.value == 500
    assert t.seconds.value == 10
    assert t.minutes.value == 1
    assert t.hours.value == 1

    expected_ticks = (
        int(500 / 1000 * 20)
        + 10 * 20
        + 1 * 60 * 20
        + 1 * 3600 * 20
    )

    assert t.ticks.value == expected_ticks

def test_at_least_one_tick():

    t = Time(Milliseconds(49))

    with pytest.raises(ValueError):
        t.ticks
