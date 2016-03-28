
$(function() {
	$( "#datepicker" ).datepicker({
	    onSelect: function(dateText, inst) {
		    var date = dateText.split('/');
		    var mes = date[0];
		    var dia = date[1];
		    var ano = date[2];


		   //  $.ajax({
     //            type:"POST",
     //            url:"seestuffs.php",
     //            data:{'mes'=mes,'dia'=dia,'ano'=ano}
     //            success: function(result)
     //            {
					// document.write(result);
     //            }
     //        });

	    	$("#porDiaDepositado").text("R$"+mes+",00");
	    	$("#porDiaSacado").text("R$"+dia+",00");
	    }
	});
});