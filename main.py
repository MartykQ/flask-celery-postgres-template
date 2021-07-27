"""
To run the app locally first run scripts/start_local_db.sh, than if running for the first time run
>> python3 manage.py recreate_db
This will start a local flask environment and will allow to run tests locally
also change MODE in .env to 'Develop'
"""

import logging

from web_app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=5011, debug=True)
    logging.info("Started app")
