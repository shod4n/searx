class SearxException(Exception):
    pass


class SearxParameterException(SearxException):

    def __init__(self, name, value):
        if value == '' or value is None:
            message = 'Empty ' + name + ' parameter'
        else:
            message = 'Invalid value "' + value + '" for parameter ' + name
        super(SearxParameterException, self).__init__(message)
        self.parameter_name = name
        self.parameter_value = value
