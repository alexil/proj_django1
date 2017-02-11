from psycopg2._psycopg import BINARY, NUMBER, STRING, DATETIME, ROWID

from psycopg2._psycopg import Binary, Date, Time, Timestamp
from psycopg2._psycopg import DateFromTicks, TimeFromTicks, TimestampFromTicks

from psycopg2._psycopg import Error, Warning, DataError, DatabaseError, ProgrammingError
from psycopg2._psycopg import IntegrityError, InterfaceError, InternalError
from psycopg2._psycopg import NotSupportedError, OperationalError

from psycopg2._psycopg import _connect, apilevel, threadsafety, paramstyle
from psycopg2._psycopg import __version__

from psycopg2 import tz
import re
def _param_escape(s,
        re_escape=re.compile(r"([\\'])"),
        re_space=re.compile(r'\s')):
    """
    Apply the escaping rule required by PQconnectdb
    """
    if not s: return "''"

    s = re_escape.sub(r'\\\1', s)
    if re_space.search(s):
        s = "'" + s + "'"

    return s

del re



def connect(dsn=None,
        database=None, user=None, password=None, host=None, port=None,
        connection_factory=None, cursor_factory=None, async=False, **kwargs):
    """
    Create a new database connection.

    The connection parameters can be specified either as a string:

        conn = psycopg2.connect("dbname=test user=postgres password=secret")

    or using a set of keyword arguments:

        conn = psycopg2.connect(database="test", user="postgres", password="secret")

    The basic connection parameters are:

    - *dbname*: the database name (only in dsn string)
    - *database*: the database name (only as keyword argument)
    - *user*: user name used to authenticate
    - *password*: password used to authenticate
    - *host*: database host address (defaults to UNIX socket if not provided)
    - *port*: connection port number (defaults to 5432 if not provided)

    Using the *connection_factory* parameter a different class or connections
    factory can be specified. It should be a callable object taking a dsn
    argument.

    Using the *cursor_factory* parameter, a new default cursor factory will be
    used by cursor().

    Using *async*=True an asynchronous connection will be created.

    Any other keyword parameter will be passed to the underlying client
    library: the list of supported parameters depends on the library version.

    """
    items = []
    if database is not None:
        items.append(('dbname', database))
    if user is not None:
        items.append(('user', user))
    if password is not None:
        items.append(('password', password))
    if host is not None:
        items.append(('host', host))
    if port is not None:
        items.append(('port', port))

    items.extend([(k, v) for (k, v) in kwargs.iteritems() if v is not None])

    if dsn is not None and items:
        raise TypeError(
            "'%s' is an invalid keyword argument when the dsn is specified"
                % items[0][0])

    if dsn is None:
        if not items:
            raise TypeError('missing dsn and no parameters')
        else:
            dsn = " ".join(["%s=%s" % (k, _param_escape(str(v)))
                for (k, v) in items])

    conn = _connect(dsn, connection_factory=connection_factory, async=async)
    if cursor_factory is not None:
        conn.cursor_factory = cursor_factory

    return conn
