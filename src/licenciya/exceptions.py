class LicenseException(Exception):
    pass


class ConfigFileNotSet(LicenseException):
    pass


class LicenseNotSubmittedYet(LicenseException):
    pass


class LicenseAlreadySubmitted(LicenseException):
    pass


class LicenseExpired(LicenseException):
    pass


class InvalidExpireIn(LicenseException):
    pass


class LicenseTooLong(LicenseException):
    pass
