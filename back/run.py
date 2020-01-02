from flask_app.core import logger
from flask_app import create_app

app = create_app()

if __name__ == '__main__':
    logger.info('Starting Template API ...')
    app.run(host='0.0.0.0', port=5000, threaded=True, ssl_context=('certs/localhost.pem', 'certs/localhost-key.pem'))
    logger.info('End of Template')
