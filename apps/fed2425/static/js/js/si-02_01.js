
$('#demo-input-search').on('input', function(e) {
    e.preventDefault();
    addrow2.trigger('footable_filter', { filter: $(this).val() });
});
var addrow2 = $('#demo-foo-addrow');
addrow2.footable().on('click', '.delete-row-btn', function() {
    var footable = addrow.data('footable');
    var row = $(this).parents('tr:first');
    footable.removeRow(row);
});

$('#demo-input-search2').on('input', function(e) {
    e.preventDefault();
    addrow3.trigger('footable_filter', { filter: $(this).val() });
});
var addrow3 = $('#demo-foo-addrow2');
addrow3.footable().on('click', '.delete-row-btn', function() {
    var footable = addrow.data('footable');
    var row = $(this).parents('tr:first');
    footable.removeRow(row);
});


$(".buscar").click();
