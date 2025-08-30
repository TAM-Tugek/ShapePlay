from shapeplay.devices import detect_device


def test_detect_device_returns_known_value():
    assert detect_device() in {"mps", "cpu"}
