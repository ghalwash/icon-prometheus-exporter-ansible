"""Test the icon_prometheus_exporter package."""


def test_version_is_string():
    import icon_prometheus_exporter
    assert isinstance(icon_prometheus_exporter.__version__, str)
