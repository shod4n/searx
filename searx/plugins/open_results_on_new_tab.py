from flask_babel import gettext
name = gettext('Open result links on new browser tabs')
description = gettext('Results are opened in the same window by default. '
                      'This plugin overwrites the default behaviour to open links on new tabs/windows. '
                      '(JavaScript required)')
default_on = False
preference_section = 'ui'

js_dependencies = ('plugins/js/open_results_on_new_tab.js',)
