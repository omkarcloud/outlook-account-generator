# chromedriver-autoinstaller-fix

chromedriver-autoinstaller-fix was created to address the "WARNING:root:Cannot find chromedriver for the currently installed Chrome version." error, which remains unresolved in the original [python-chromedriver-autoinstaller](https://github.com/yeongbin-jo/python-chromedriver-autoinstaller) repository. 

By using chromedriver-autoinstaller-fix, you shouldn't encounter installation errors if you're using Chrome versions greater than 115.

## Installation

```bash
pip install chromedriver-autoinstaller-fix
```

## Usage
Just type `import chromedriver_autoinstaller_fix` in the module you want to use chromedriver.

## Example
```
from selenium import webdriver
import chromedriver_autoinstaller_fix


chromedriver_autoinstaller_fix.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
```

## Would appreciate a Star :)