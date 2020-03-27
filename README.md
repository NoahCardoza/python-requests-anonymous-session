# Python Requests – Anonymous Session

> Randomizes the user agent, and applies the default headers and cipher suite found in that browser.

## Installation

```bash
pip install python-requests-anonymous-session
```

## Useage

Note: `AnonymousSession` inherits from `requests.Session`.

### Simple

```py
from python_requests_anonymous_session import AnonymousSession

session = AnonymousSession()
```

### Advanced

Choose wether you want to use mobile/desktop broswer profiles

```py
session = AnonymousSession(browser={
    'desktop': False,   # default True,
    'mobile': True,     # default True,
})
```

### Slightly More Advanced

Choose which `user-agent` you want. If the `user-agent` is in found in our database the correct default headers
and cipher suite will be applied.

```py
session = AnonymousSession(browser={
    'custom': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
})
```

## Credits

+ [VeNoMouS/cloudscraper](https://github.com/VeNoMouS/cloudscraper) for the [browsers.json](python_requests_anonymous_session/browsers.json)
  file and the original `UserAgent` and `CipherSuiteAdapter` implementations.
