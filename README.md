# A Practical Method for High-Resolution Burned Areas Monitoring using Sentinel-2 and VIIRS 



## Install using pip

`pip install FireHR`

## Install from repo
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
