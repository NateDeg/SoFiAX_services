## Tests

A suite of functional tests to ensure the deployment is working correctly. To run these tests you will need to set up the environment with the following steps.

### 1. Install + deploy

See repo [README](/README.md) for deploying the HI source finding portal services and database.

We need specific python libraries for running the tests. Install the requirements:

```
pip install -r tests/requirements.txt
```

You will also need to install a webdriver for automated web testing. You can download the Firefox webdriver from:

- https://github.com/mozilla/geckodriver/releases

### 2. Injest data

#### 1. Download test data

[Download link](https://www.dropbox.com/scl/fi/cpvwons59hek6ywikfbzf/HI_source_finding_portal_test_data.tar.gz?rlkey=5zzupfwlptki6hmytmelme2qj&st=nml29vtm&dl=0)

These are outputs and product files generated by SoFiA-2 applied to cutouts of WALLABY with SBIDs 51506 and 51535.

**Note**: You will need to change the `config.ini` files and the `sofia_00X.par` files with updated `output.directory` parameters with the full path of the downloaded product files. These files are found in the `/outputs` subdirectories.

#### 2. Run [SoFiAX](https://github.com/AusSRC/SoFiAX)

For both SBIDs you will need to run

```
python -m sofiax -c $DIR/config.ini \
    -p $DIR/sofia_001.par $DIR/sofia_002.par $DIR/sofia_003.par $DIR/sofia_004.par
```

replacing `$DIR` with the location of the downloaded test data files.

#### 3. Run `dss_image` scripts for summary plots (optional)

You can generate summary figures for detections made using SoFiA-2 using the code available at: https://github.com/AusSRC/pipeline_components/tree/main/dss_image. It can be run as follows

```
python get_dss_image.py -r $RUN_NAME
```

replacing `$RUN_NAME` with the SBID folder name in the test data files. The summary figures will then appear when viewing the detections.

### 3. Running test suite

- Create [`.env`](/tests/.env) pointing to the URL of the web service, the admin user credentials and information about the project (web configuration items)

```
URL = "127.0.0.1"
USERNAME = "admin"
PASSWORD = "admin"
TITLE = "survey"
```

Then run the tests pointing to the development environment

```
pytest
```
