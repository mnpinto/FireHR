[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1xrI2lZmqjkgnFzskl-VZFDExYeOrr-en)

For help with the library join my discord server: https://discord.gg/vpnTAw4q62

# A Practical Method for High-Resolution Burned Area Monitoring using Sentinel-2 and VIIRS 
Article: https://www.mdpi.com/2072-4292/13/9/1608

## Install the lastest stable version using pip

`pip install FireHR==0.1.1`

**Warning:** version 0.1.2 has some bugs that still need fixing. Make sure you use version 0.1.1 unless you are just using the Sentinel-2 data download utility as shown in this notebook: https://colab.research.google.com/drive/1CqerpiyWeFty396VZPov_mGe7YBHHlKs

## Install development version from repo
```bash
git clone https://github.com/mnpinto/FireHR
cd FireHR; pip install -e .
```

## How to use

#### Configuration of Google Earth Engine API
Run the following python code and follow the link to generate the authentication file:
```python
import ee
ee.Authenticate()
```
Once you are done you should see the message `Successfully saved authorization token.` and the file `~/.config/earthengine/credentials` should exist. 

Please refer to https://developers.google.com/earth-engine/guides/python_install for more information about the GEE Python API. 

#### Command line utility to run FireHR for an event as outputed by BA-Net post-processing
```bash
firehr_from_banet_events ba100m_PT2020_218.tif
```

Optional arguments:

|Argument|default|type|description|
|---|---|---|---|
|path| '.' | str |Path to save the outputs.|
|composite_days_before| 120 |int| Time window size in days for the pre-fire data |
|composite_days_after| 120 |int| Time window size in days for the post-fire data |
|max_cloud_fraction| None |float (0.0-1.0)| Remove images with a cloud fraction higher than specified |
|use_least_cloudy | None |int| Select the n least cloudy images in the time_window |

Example using `use_least_cloudy` parameter:
```bash
firehr_from_banet_events ba100m_PT2020_218.tif --use_least_cloudy 5
```
