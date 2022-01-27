# CSMoney Market Monitoring System
## Overview
Service for csmoney market monitoring and creating our DB, will 
pull history of prices for item and in future will monitor market
once at some time to extend a price history by new data.
## Setup
Install the dependencies:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
## Usage
### Main service:
```bash
$ export FLASK_APP=main.py # set default server app
$ flask run # run server
```
### Celery workers:
```bash
# collecting data worker
$ celery -A background.celery_app.app worker -Q csmoney_queue
# worker to keep main database updated
$ celery -A background.celery_app.app worker -Q items_base_queue
# worker to keep service database updated
$ celery -A background.celery_app.app worker -Q broadcast_provider
```

## CSMONEY API
### Examples:
* https://cs.money/skin_info?appId=570&id=1510356&isBot=true&botInventory=true
* https://inventories.cs.money/5.0/load_bots_inventory/570?limit=60&offset=0&order=desc&sort=price&withStack=true