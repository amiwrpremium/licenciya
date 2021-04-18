from licenciya import Licenciya


def main():
    li = Licenciya()
    li.make_config_file('Data.ini')
    li.set_server_submit_url('https://amiwr-license.herokuapp.com/submit-license')
    li.set_server_validate_url('https://amiwr-license.herokuapp.com/validate-license')

    li.submit_license()

    if li.validate_license():
        print('Valid License')
    else:
        print('Invalid License')


if __name__ == '__main__':
    main()

