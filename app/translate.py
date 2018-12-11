import json
import requests
from flask_babel import gettext as _

from app import app


def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY']}
    endpoint = 'https://api.microsofttranslator.com/v2/Ajax.svc/Translate'
    params = '?text={}&from={}&to={}'.format(text, source_language, dest_language)
    r = requests.get(endpoint + params, headers=auth)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))
