# make a file
#
# C:\Users\rasmu\api_credentials_xolta.ini
#
# and enter data like this :
#
#
# [api_credentials]
# username = <email>
# password = <password>

# [api_xolta_id]
# device-id = <id>
# site-id = <id>
#
import configparser

# change the location to your own
config_file_path = r'C:\Users\rasmu\api_credentials_xolta.ini'

config = configparser.ConfigParser()
config.read(config_file_path)

api_username = config.get('api_credentials', 'username')
api_password = config.get('api_credentials', 'password')

api_deviceid = config.get('api_xolta_id', 'device-id')
api_siteid = config.get('api_xolta_id', 'site-id')
