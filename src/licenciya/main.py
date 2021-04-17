import uuid
import requests

import configparser
import os

import exceptions


class Licenciya:
    def __init__(self):
        self.config = None
        self.server_submit_url = None
        self.server_validate_url = None

        self.pc_uuid = self.get_pc_uuid()

        self.config_file_set = False

        pass

    @staticmethod
    def get_pc_uuid() -> str:
        return str(uuid.UUID(int=uuid.getnode()))

    def set_server_submit_url(self, url: str) -> None:
        self.server_submit_url = url

    def set_server_validate_url(self, url: str) -> None:
        self.server_validate_url = url

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
        if self.server_submit_url:
            if not self.license_is_added():
                user_license = input("Enter License: ")
                self.update_first_run(user_license)
                url = self.server_submit_url
                data = {
                    'UUID': self.pc_uuid,
                    'LICENSE': user_license,
                }

                try:
                    r = requests.post(url, data=data)
                except Exception as e:
                    return False

                if r.status_code == 200:
                    return True
                else:
                    return False
            else:
                pass
        else:
            raise exceptions.ServerValidateUrlNotSet

    def validate_license(self):
        user_license = self.get_license()
        if self.server_validate_url:
            url = self.server_validate_url
            params = {
                'UUID': self.pc_uuid,
                'LICENSE': user_license,
            }
            try:
                r = requests.get(url, params=params)
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
        else:
            raise exceptions.ServerValidateUrlNotSet
