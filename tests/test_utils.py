def test_get_chrome_version():
    from chromedriver_autoinstaller_fix.utils import get_chrome_version

    version = get_chrome_version()
    assert version is None or version.count(".") == 3
