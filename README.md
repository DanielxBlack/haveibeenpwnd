# python bindings for HaveIBeenPwnd.com V2

Troy Hunt released a new version of the `Have I Been pwnd Database`. This time with more anonymity
in mind.

## Features:

* does not sent passwords to HaveIBeenPwnd.com
* does not sent complete password hashes to HaveIBeenPwnd.com
* zero dependencies except requests (will be removed later)
* python2 & python3 support
* tests

## Usage:

Straight forward:

    >>> from haveibeenpwnd import check_password
    >>> check_password('hunter2')
    16092
    >>> check_password('lksdflksdpsökfdsödg')
    0

## Installation

You can install haveibeenpwnd with pip:

    $ pip install haveibeenpwnd


## Testing:

You can run tests with:

    $ tox

