$( document ).ready(function() {
    console.log("main");
    $( ".custom-dropdown " ).change(function(e) {
        var contentPanelId = jQuery(this).attr("href");

        var scoring = $(".custom-dropdown :selected").attr("value");

        if (scoring === "PPR") {
            location.href='/rankings/ppr';
        }
        if (scoring === "Standard") {
            location.href='/rankings/standard';
        }
        if (scoring === "Half") {
            location.href='/rankings/half';
        }
    });


});





