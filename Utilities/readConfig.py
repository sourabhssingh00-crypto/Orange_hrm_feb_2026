import configparser
config = configparser.RawConfigParser()
# config.read(r"C:\credence\orange_hrm_framework\Configuration\config.ini")
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def get_username():
        username = config.get("login", "username")
        return username

    @staticmethod
    def get_password():
        return config.get("login", "password")

    @staticmethod
    def get_login_url():
        return config.get("urls", "login_url")



