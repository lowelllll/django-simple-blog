var he = $(window).height();
$("#wrap").height(he);

$("#wrap").resize(function(){
    var he = $(window).height();
    $("#wrap").height(he);
});
