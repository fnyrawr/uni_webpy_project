$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.materialboxed').materialbox();
    $('.modal').modal();
    $('.rateYo').rateYo({
        starWidth: "20px"
    });

    $("#rateyo_review_stars").rateYo()
    .on("rateyo.set", function (e, data) {
        if(data.rating < 1) data.rating = 1;
        if(data.rating > 5) data.rating = 5;
        document.getElementById("id_stars").value = data.rating;
    })
    .on("rateyo.change", function (e, data) {
        if(data.rating < 1) data.rating = 1;
        if(data.rating > 5) data.rating = 5;
        document.getElementById("review_stars").innerHTML = data.rating + ' Stars';
    });

    $("#rateyo_stars").rateYo()
    .on("rateyo.set", function (e, data) {
        if(data.rating < 1) data.rating = 1;
        if(data.rating > 5) data.rating = 5;
        document.getElementById("id_sortStarsBy").value = data.rating;
    })
    .on("rateyo.change", function (e, data) {
        if(data.rating < 1) data.rating = 1;
        if(data.rating > 5) data.rating = 5;
        document.getElementById("chip_stars").innerHTML = data.rating + ' Stars';
    });
});