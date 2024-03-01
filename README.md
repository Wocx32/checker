# Usage
Install requirements
```bash
pip install -r requirements.txt
```

Start server
```bash
python app.py
```

Test by running `check.py`
```
python check.py
```

# Note regarding testcases

Testcases should start with the prefix `test_` and rest should be the name of the function under test. For example we have function: `harness_solar_energy`, the testcase should be `test_harness_solar_energy`, otherwise it won't work.


# For making new testcases

To make testcases for new assignments or labs, use the format `test_{assignment/lab}`. Please note that the url generated will be the module name without `test_`, for example `test_a1.py` will generate the url `/test/a1`, similarly `test_lab01.py` will generate `/test/lab01`.