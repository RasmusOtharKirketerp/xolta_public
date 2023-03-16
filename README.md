
This will launch a python plots and displays the battery status, solar cell production, and electricity grid consumption metrics for the last many days day. 

Exports plot to .png and csv files (see pictures in this repo)

## Data Sources

The data for this program is sourced from your XOLTA battery system. The data is collected almost real-time.

## Visualization Examples

### Battery Status

The following gauge shows the current battery status for the last 7 days:

![Battery Status](https://user-images.githubusercontent.com/15995296/224811427-6f456238-dc2c-4dc5-8af7-408b9ab6346e.png)

### Solar Cell Production

The following line chart shows the solar cell production over the last 7 days:

![Solar Cell Production](https://user-images.githubusercontent.com/15995296/224811558-3380118c-eccc-4434-ad55-f6667eb4b386.png)

### Electricity Grid Consumption

The following line chart shows the electricity grid consumption over the last 7 days:

![Electricity Grid Consumption](https://user-images.githubusercontent.com/15995296/224811609-42d8c464-0936-4321-ac3b-8608f41eaeba.png)

## Setup

### Create a config file contaning this :
[api_credentials]
username = <email>
password = <password>

[api_xolta_id]
device-id = <id>
site-id = <id>

and point to this file in get_config.py

### how to find device-id and site-id
To find your device
* login your app.xolta.com
  ![image](https://user-images.githubusercontent.com/15995296/224817946-979d9b31-2e5b-45d1-8e38-3c15fd41ab3e.png)

To find site-id open dev.tools and find the site-id here : (the device-id is also here)
  * ![image](https://user-images.githubusercontent.com/15995296/224819502-9cd78102-55b8-4ee0-ae88-e812d3c075c4.png)



## Here's a brief overview of each file:

api_data.py: This file contains the get_data() function that sends an API request to the Xolta server and returns the telemetry data.

bearerCache.py: This file caches the authentication token to avoid making unnecessary requests for new tokens. It also provides the get_auth_with_renewal() function to automatically refresh the token when it expires.

data_formatting.py: This file formats the telemetry data into a pandas DataFrame.

datapunkter.py: This file defines the telemetry fields used in the project.

get_config.py: This file reads API credentials and device/site IDs from a configuration file.

plot_data.py: This file contains the plot_data() function that uses Matplotlib to visualize the telemetry data.

stack_days_one_color.py: This is the main script that fetches the data, formats it, and plots it using the functions from the other files.

xolta_get_auth.py: This file provides the XoltaBattAuthenticator class, which handles the authentication process using Selenium WebDriver.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to https://github.com/AThomsen for making the get token stuff
