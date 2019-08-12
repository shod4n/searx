if(searx.autocompleter) {
    searx.searchResults = new Bloodhound({
        datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
        queryTokenizer: Bloodhound.tokenizers.whitespace,
        remote: './autocompleter?q=%QUERY'
    });
    searx.searchResults.initialize();
}

$(document).ready(function(){ 
    if(searx.autocompleter) {
        $('#q').typeahead(null, {
            name: 'search-results',
            displayKey: function(result) {
                return result;
            },
            source: searx.searchResults.ttAdapter()
        });
    }
});
