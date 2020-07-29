
class ParserTemplateFileException(Exception):
    """Raised when a template file cannot be parsed."""
    __name__ = 'ParserTemplateFileException'


class ParserTemplateValueException(Exception):
    """Raised when an invalid template value is encountered"""
    __name__ = 'ParserTemplateValueException'
