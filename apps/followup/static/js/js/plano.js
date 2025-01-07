$('input[name="myradio"]').change(function(e) {
    if($(this).val() == 'r_r40'){
        $(".r40").show();
        $(".r40_doc").hide();
    }
    if($(this).val() == 'r_doc'){
        $(".r40_doc").show();
        $(".r40").hide();
    }
});