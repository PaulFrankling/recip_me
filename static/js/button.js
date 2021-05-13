//  Credit: https://forum.squarespace.com/topic/190117-back-to-top-button-make-it-appeardisappear-on-scroll/

// Back to top button
$(document).ready(function () {

    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('a.btn-floating').fadeIn(); // Fades the button in scrolling down the page
        } else {
            $('a.btn-floating').fadeOut(); // Fades the button out going to the top of page
        }
    });
    $('.btn-floating').click(function () {
        $("html, body").animate({
            scrollTop: 0 // Takes user to the very top of the page
        }, 200); // Speed of scroll 
        return false;
    });

});