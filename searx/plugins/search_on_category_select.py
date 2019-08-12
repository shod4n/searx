
from flask_babel import gettext
name = gettext('Search on category select')
description = gettext('Perform search immediately if a category selected. '
                      'Disable to select multiple categories. (JavaScript required)')
default_on = True
preference_section = 'ui'

js_dependencies = ('plugins/js/search_on_category_select.js',)
