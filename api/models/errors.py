# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueDoesNotMatchRegExpError(Error):
    """Raised when the input value does not match to regular expression"""
    pass


class ValueTooLong(Error):
    """Raised when the input value is too long"""
    pass


class ValueIsInCodenamesDictionary(Error):
    """Raised when the input value is already in codenames dictionary"""
    pass
