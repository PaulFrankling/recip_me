//  Credit: https://forum.squarespace.com/topic/190117-back-to-top-button-make-it-appeardisappear-on-scroll/

// Back to top button
$(document).ready(function () {

    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('a.btn-floating').fadeIn();
        } else {
            $('a.btn-floating').fadeOut();
        }
    });
    $('.btn-floating').click(function () {
        $("html, body").animate({
            scrollTop: 0
        }, 200);
        return false;
    });

});