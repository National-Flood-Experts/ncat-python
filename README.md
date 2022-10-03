# ncat-python

A python wrapper for the NGS’s Coordinate Conversion and Transformation Tool (NCAT) API. More information about the API is available [here](https://www.ngs.noaa.gov/web_services/ncat/index.shtml).

## Features
- Can make calls to all 5 NCAT services (LLH, SPC, UTM, XYZ, and USNG)
- Ensures required parameters for different NCAT services are present before making api call.

## Installation
Using pip:
```commandline
pip install ncat-api
```

## Usage
To use the package: 

```python
import NCAT from ncatapi
```

## Making Requests
### LLH Request
Perform an LLH Service request.
```python
from ncatapi import NCAT

ncat = NCAT()
response = ncat.llh({
            'lat': 40.0,
            'lon': -80.0,
            'orthoHt': 99.0,
            'inDatum': 'nad83(1986)',
            'outDatum': 'nad83(2011)',
            'inVertDatum': 'NGVD29',
            'outVertDatum': 'NAVD88'
        })
```
#### Sample Response:
```text
{
    'ID': '1664818932872', 
    'nadconVersion': '5.0',
     'vertconVersion': '3.0', 
     'srcDatum': 'NAD83(1986)', 
     'destDatum': 'NAD83(2011)', 
     'srcVertDatum': 'NGVD29', 
     'destVertDatum': 'NAVD88', 
     'srcLat': '40.0000000000', 
     'srcLatDms': 'N400000.00000', 
     'destLat': '39.9999983008',
     'destLatDms': 'N395959.99388',
     'deltaLat': '-0.189',
     'sigLat': '0.000263',
     'sigLat_m': '0.0081',
     'srcLon': '-80.0000000000',
     'srcLonDms': 'W0800000.00000',
     'destLon': '-79.9999976143',
     'destLonDms': 'W0795959.99141',
     'deltaLon': '0.204',
     'sigLon': '0.000221',
     'sigLon_m': '0.0052',
     'heightUnits': 'm',
     'srcEht': 'N/A',
     'destEht': 'N/A',
     'sigEht': 'N/A',
     'srcOrthoht': '99.000',
     'destOrthoht': '98.848',
     'sigOrthoht': '0.005',
     'spcZone': 'PA S-3702',
     'spcNorthing_m': '76,470.391',
     'spcEasting_m': '407,886.681',
     'spcNorthing_usft': '250,886.607',
     'spcEasting_usft': '1,338,208.220',
     'spcNorthing_ift': '250,887.109',
     'spcEasting_ift': '1,338,210.896',
     'spcConvergence': '-01 27 35.22',
     'spcScaleFactor': '0.99999024',
     'spcCombinedFactor': 'N/A',
     'utmZone': 'UTM Zone 17',
     'utmNorthing': '4,428,235.878',
     'utmEasting': '585,360.668',
     'utmConvergence': '00 38 34.18',
     'utmScaleFactor': '0.99968970',
     'utmCombinedFactor': 'N/A',
     'x': 'N/A',
     'y': 'N/A',
     'z': 'N/A',
     'usng': '17SNE8536128236'
 }
```

### SPC Request
Perform an SPC Service request.
```python
from ncatapi import NCAT

ncat = NCAT()
response = ncat.spc({
    'northing': 173099.419,
    'easting': 503626.812,
    'spcZone': 2402,
    'inDatum': 'nad83(2011)',
    'outDatum': 'nad83(NSRS2007)'
})
```

### USNG Request
Perform an USNG Service request.
```python
from ncatapi import NCAT

ncat = NCAT()
response = ncat.usng({
    'usng': '15SWB4788338641',
    'inDatum': 'nad83(2011)',
    'outDatum': 'nad83(NSRS2007)'
})
```

### UTM Request
Perform an UTM Service request.
```python
from ncatapi import NCAT

ncat = NCAT()
response = ncat.utm({
    'northing': 4138641.144,
    'easting': 547883.655,
    'utmZone': 15,
    'spcZone': 2401,
    'inDatum': 'NAD83(2011)',
    'outDatum': 'NAD83(NSRS2007)'
})
```

### XYZ Request
Perform an XYZ Service request.
```python
from ncatapi import NCAT

ncat = NCAT()
response = ncat.xyz({
    'x': -217687.279,
    'y': -5069012.406,
    'z': 3852223.048,
    'inDatum': 'NAD83(2011)',
    'outDatum': 'NAD83(NSRS2007)'
})
```
