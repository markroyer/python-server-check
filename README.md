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

## Basic Usage

The script can be executed in the following manner.

```bash
usage: checkServer.py [-h] [-a ATTEMPTS] [-w WAIT] [-g]
                      host sender recipients [recipients ...]

positional arguments:
  host                  host name to verify
  sender                email sender
  recipients            email recipients

optional arguments:
  -h, --help            show this help message and exit
  -a ATTEMPTS, --attempts ATTEMPTS
                        max attempts
  -w WAIT, --wait WAIT  wait time in seconds (default: 20)
  -g, --wget            use wget instead of icmp ping
```

As an example, invoking the script as

```bash
./checkServer.py foo.com a@email.com b@email.com
```

checks to see if `foo.com` reachable by ping.  If `foo.com` is not
reachable, an email is sent from `a@email.com` to `b@email.com`.

Using the `--wget` option allows you to specify an alternative port if
icmp traffic is blocked or ignored.  Specify the port by appending it
to the host name.  For example, specify `foo.com:8080` would use wget
to check for the default page served on port **8080**.

## Using Cron

If you are using this script, then you probably want to use it with cron.

Typing

```
crontab -e
```

at a terminal will allow you to edit the local user's cron job file.

Adding a line such as

```
*/30 * * * * ~/checkServer.py foo.com a@email.com b@email.com
```

will check every 30 minutes that the server is still accessible.  This
assumes that the `checkServer.py` is placed in your home directory and
is executable.

## License

The project is licensed under the terms of the
[GPL3](https://www.gnu.org/licenses/gpl-3.0.en.html) license.

<!--  LocalWords:  sendmail checkServer py wget icmp Cron cron
 -->
<!--  LocalWords:  crontab
 -->
