# Citi Bike Application

## Data Source
- Citi Bike Data Location
  - https://s3.amazonaws.com/tripdata/index.html
- Citi Bike Data Usage Policy
  - https://ride.citibikenyc.com/data-sharing-policy


## Running Application
- Download the code repository
- Ensure python 3 is installed on you local machine with pip
- There are certain python packages that are necessary for the application to run. You can install through the below command in powershell. **Fix This**

```shell
cd citi_app
pip install -r requirements.txt
```

- Run the below command to install the application packages
```shell
pip install -e .
python
```

- Execute below command to run the application
```shell
from citi_app.run_pipeline import run_pipeline
run_pipeline()
```

## Objectives

### Bayesian and Frequentist Statistics