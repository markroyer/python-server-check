# python-server-check

A simple Python script to see if a server is still alive. If the
server does not respond after 10 ping attempts, the script will email
recipients indicated in the script.

## Requirements

The program requires Python and some email daemon to be installed (eg,
sendmail).

## Building

No need to build anything.  However, you will want to modify the
script to send email to the appropriate people.  After modifications,
just run using the Python interpreter.

## Using Cron

If you are using this script, then you probably want to use it with cron.

Typing

```
crontab -e
```

at a terminal will allow you to edit the local user's cron job file.

Adding a line such as

```
*/30 * * * * ~/checkServer.py
```

will check every 30 minutes that the server is still accessible.  This
assumes that the `checkServer.py` is placed in your home directory and
is executable.

## License

The project is licensed under the terms of the
[GPL3](https://www.gnu.org/licenses/gpl-3.0.en.html) license.
