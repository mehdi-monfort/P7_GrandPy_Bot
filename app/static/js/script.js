$(function() {
  
	var $list, $newItemForm;
	$list = $('div');
	$newItemForm = $('#newItemForm');

	$newItemForm.on('submit', function(validate) {
	validate.preventDefault();
	var text = $('input:text').val();
	$list.text(text);
	$('input:text').val('');
	});

});