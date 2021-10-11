crlf
----
git config --global core.autocrlf false

Usually dos2unix is enough, but today, that is not enough, possibly
because docker isn't detecting the crlf change as a change.


pipenv install --dev --skip-lock
--------------------------------
pylibmc - maintainer says he will not support windows. Might be able to get this to install anyhow
if header files in right place.

Not sure why pylibmc is needed, this appears to be a way of installing memcached

Also, if you install locally on windows, after touching the Pipfile.lock, it will likely fail in the docker build.

docker-compose up
-----------------
ERROR: for db  Cannot start service db: Ports are not available: listen tcp 0.0.0.0:54323: bind: An attempt was made to access a socket in a way forbidden by its access permissions.
https://stackoverflow.com/questions/65272764/ports-are-not-available-listen-tcp-0-0-0-0-50070-bind-an-attempt-was-made-to

Bash files will get copied with wrong line endings, so you must run dos2unix before docker build on *.sh
