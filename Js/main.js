

var altura = $("navbar").offset().top;
$(window).on("scroll", function(){
    if ($(window).scrollTop() > (50)) {
        $("navbar").addClass("shrink");
    } else {
        $("navbar").removeClass("shrink");
        $("navbar").addClass("shrink")
}
})

