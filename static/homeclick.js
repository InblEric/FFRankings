$( document ).ready(function() {
    console.log("main");
    $( "  #voting p a" ).click(function(e) {
        console.log( "clicked on " );
        var contentPanelId = jQuery(this).attr("href");
        console.log(contentPanelId);

        var scoring = $(".custom-dropdown :selected").attr("value");
        console.log("scoring was")
        console.log(scoring)

        //MAKE THIS SAFE
        if (scoring === "PPR") {
            $(this).attr("href", contentPanelId + "/" + scoring);
        }
        if (scoring === "Standard") {
            $(this).attr("href", contentPanelId + "/" + scoring);
        }
        if (scoring === "Half") {
            $(this).attr("href", contentPanelId + "/" + scoring);
        }

        $( this ).off( "click", "**" );

        $(this).click()
    });


});





