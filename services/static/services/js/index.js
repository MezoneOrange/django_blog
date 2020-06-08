/**
 * Add 'activate' class to navigation link when you in the page
 * that has same link.
 */
;(function($, undefined) {
    $(document).ready(function () {
        let url = location.href;
        let pattern = url.replace(/[\w]{4,5}:\/\/[\d\w\.]+:*[\d]*/i, "");
        for (i of [1, 2, 3]) {
            let item = $("#link_" + i).attr('href');
            if (pattern == item) {
                $("#link_" + i).addClass("active");
            } else {
                $("#link_" + i).removeClass("active");
            }
        }


    });
})(jQuery);
