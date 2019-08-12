window.searx = (function(d) {
    'use strict';

    // add data- properties
    var script = d.currentScript  || (function() {
        var scripts = d.getElementsByTagName('script');
        return scripts[scripts.length - 1];
    })();

    return {
        autocompleter: script.getAttribute('data-autocompleter') === 'true',
        method: script.getAttribute('data-method')
    };
})(document);
