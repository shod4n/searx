from flask_babel import gettext
import re
from searx.url_utils import urlunparse

regexes = {re.compile(r'utm_[^&]+&?'),
           re.compile(r'(wkey|wemail)[^&]+&?'),
           re.compile(r'&$')}

name = gettext('Tracker URL remover')
description = gettext('Remove trackers arguments from the returned URL')
default_on = True
preference_section = 'privacy'


def on_result(request, search, result):
    query = result['parsed_url'].query

    if query == "":
        return True

    for reg in regexes:
        query = reg.sub('', query)

    if query != result['parsed_url'].query:
        result['parsed_url'] = result['parsed_url']._replace(query=query)
        result['url'] = urlunparse(result['parsed_url'])

    return True
