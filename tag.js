$(document).ready(function(){
	var raw = $('#source').text();
	var listType = 'ul';
	var dataAttr = 'yes';
	
	$('#convert').on('click', function(event){
		raw = $('#source').val();
		listType = $('#radio-ol')[0].checked ? 'ol' : 'ul';
		dataAttr = ($('#data-attr')[0].checked) ? 'yes' : 'no';
		$.ajax({
			url: "https://wwwx.cs.unc.edu/~duozhao/app/html-list/connector.php",
			type: "GET",
			data: { 'source': raw, 'listType': listType, 'dataAttr': dataAttr},
			cache: false
		}).done(function(html) {
			$("#target").html(html);
		});
	});

	$('#convert').trigger('click');

	$("#input-field").on('keydown', '#source', function(e) { 
		var keyCode = e.keyCode || e.which;
		if (keyCode == 9) { 
			var start = this.selectionStart;
			var end = this.selectionEnd;
			var value = $(this).val();
			$(this).val(value.substring(0, start) + "\t"
					+ value.substring(end));
			this.selectionStart = this.selectionEnd = start + 1;
			e.preventDefault();
		}else{
			$('#convert').trigger('click');
		}
	});

	$('#radio-ul').on('click', function(){
		$('#convert').trigger('click');
	});

	$('#radio-ol').on('click', function(){
		$('#convert').trigger('click');
	});
	
	$('#data-attr').on('click', function(){
		$('#convert').trigger('click');
	});
	
});


