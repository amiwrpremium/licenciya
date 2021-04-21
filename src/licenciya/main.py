import configparser
import os
import uuid

import requests

from . import exceptions

base_url = "http://127.0.0.1:5000/api/v1/"


class Licenciya:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

        self.params = {
            'api_key': self.api_key,
            'api_secret': self.api_secret,
        }

        self.config = None
        self.config_file_set = False

        self.pc_uuid = str(uuid.UUID(int=uuid.getnode()))

    def make_config_file(self, filename: str) -> None:
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write("[DEFAULTS]\nlicense = None")

        self.config = configparser.ConfigParser()
        self.config.read(filename)
        self.config_file_set = True

    def license_is_added(self) -> bool:
        _ = self.config['DEFAULTS'].get('license')
        if _ == 'None':
            return False
        else:
            return True

    def get_license(self):
        if self.config_file_set:
            _ = self.config['DEFAULTS'].get('License')
            if _:
                return _
            else:
                raise ValueError('Value Error At Config File')
        else:
            raise exceptions.ConfigFileNotSet

    def update_first_run(self, user_license):
        self.config.set('DEFAULTS', 'License', user_license)
        with open('Data.ini', 'w') as configfile:
            self.config.write(configfile, space_around_delimiters=True)
            configfile.close()

    def update_first_run_fail(self):
        self.config.set('DEFAULTS', 'License', "None")
        with open('Data.ini', 'w') as configfile:
            self.config.write(configfile, space_around_delimiters=True)
            configfile.close()

    def submit_license(self):
        url = base_url + "submit-license"
        if not self.license_is_added():
            user_license = input("Enter License: ")
            self.update_first_run(user_license)

            data = {
                'uuid': self.pc_uuid,
                'license': user_license,
            }

            try:
                r = requests.post(url, data=data, params=self.params)
            except Exception as e:
                return False

            if r.status_code == 200:
                return True
            else:
                return False
        else:
            pass

    def validate_license(self):
        url = base_url + "validate-license"
        user_license = self.get_license()

        data = {
            'uuid': self.pc_uuid,
            'license': user_license,
        }
        try:
            r = requests.post(url, data=data, params=self.params)
        except Exception as e:
            self.update_first_run_fail()
            return False

        if r.status_code == 200:
            response = r.json()
            is_licensed = response['licensed']
            if is_licensed:
                return True
            else:
                self.update_first_run_fail()
                return False
        else:
            self.update_first_run_fail()
            return False
