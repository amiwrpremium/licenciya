import requests
from . import exceptions
from warnings import warn


class AdminManageLicense:
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret

        self.params = {
            'api_key': self.api_key,
            'api_secret': self.api_secret
        }

    def new_license(self, license_key: str, expire_in: int):
        if not type(expire_in) == int:
            raise exceptions.InvalidExpireIn('expire_in must be integer')

        if expire_in <= 0:
            raise exceptions.InvalidExpireIn('expire_in must be positive')

        if len(license_key) >= 50:
            raise exceptions.LicenseTooLong('wtf?')

        url = 'https://amiwr-license.herokuapp.com//api/v1/admin-submit'

        data = {
            'license': license_key,
            'expire': expire_in,
        }

        r = requests.post(url, data=data, params=self.params)

        return r.json()

    def remove_license(self, license_key: str):
        url = 'https://amiwr-license.herokuapp.com/api/v1/admin-remove'

        data = {
            's': license_key
        }

        r = requests.post(url, data=data, params=self.params)

        return r.json()

    @staticmethod
    def retrieve_all_license():
        warn('Under Maintenance')
