
// Top Carousel
$(document).ready(function () {
    // Activate my Top Carousel
    $("#myTopCarousel").carousel();

// Enable Carousel Indicators
    $(".item1").click(function () {
        $("#myTopCarousel").carousel(0);
    });
    $(".item2").click(function () {
        $("#myTopCarousel").carousel(1);
    });
    $(".item3").click(function () {
        $("#myTopCarousel").carousel(2);
    });

// Enable Carousel Controls
    $(".left").click(function () {
        $("#myTopCarousel").carousel("prev");
    });
    $(".right").click(function () {
        $("#myTopCarousel").carousel("next");
    });
});

$(document).ready(function () {
    // Newest Cactuses
    $('.owl-carousel').each(function () {
        $(this).owlCarousel({
            loop : true,
            margin : 10,
            nav : false,
            responsive:{
                0:{
                    items:1
                },
                600:{
                    items:3
                },
                1000:{
                    items:5
                }
            }
        });
    });

});

