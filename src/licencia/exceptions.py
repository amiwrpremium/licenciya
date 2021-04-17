class LicenseException(Exception):
    pass


class ConfigFileNotSet(LicenseException):
    pass


class ServerSubmitUrlNotSet(LicenseException):
    pass


class ServerValidateUrlNotSet(LicenseException):
    pass


class LicenseNotSubmittedYet(LicenseException):
    pass


class LicenseAlreadySubmitted(LicenseException):
    pass
