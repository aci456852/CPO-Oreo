import functools


class loging(object):
    def __init__(self, level="warn") -> None:
        self.level = level

    def __call__(self, func):
        @functools.wraps(func)
        def _deco(*args, **kwargs):
            if self.level == "warn":
                self.notify(func)
            return func(*args, **kwargs)
        return _deco

    def notify(self, func) -> None:
        print("%s is running" % func.__name__)


@loging(level="warn")
def bar_A(a: int, b: int) -> str:
    a = ('i am bar:%s' % (a+b))
    return a


# inheritances
class email_loging(loging) :
    def __init__(self, email='1084665808@qq.com', *args, **kwargs) -> None:
        self.email = email
        super(email_loging, self).__init__(*args, **kwargs)

    def notify(self, func) -> None:
        print("%s is running" % func.__name__)
        print("sending email to %s" % self.email)


@email_loging(level="warn")
def bar_B(a: int, b: int) -> str:
    b = ('i am bar:%s' % (a+b))
    return b


# multiple inheritances
class second_email_loging(email_loging):
    def __init__(self, second_email='1262687293@qq.com', *args, **kwargs) -> None:
        self.second_email = second_email
        super(email_loging, self).__init__(*args, **kwargs)

    def notify(self, func) -> None:
        print("%s is running" % func.__name__)
        print("sending second_email to %s" % self.second_email)


@second_email_loging(level="warn")
def bar_C(a: int, b: int) -> str:
    c = ('i am bar:%s' % (a+b))
    return c