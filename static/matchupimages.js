$( document ).ready(function() {
    console.log("main");

});

var myFuncOne = function(playerURL) {
    var img = $( "#player1pic" ).load( playerURL + " .player-photo" );
};

var myFuncTwo = function(playerURL) {
    var img = $( "#player2pic" ).load( playerURL + " .player-photo" );
};



