$(document).ready(function () {
    $('.navbar-burger').click(function () {
        $(this).toggleClass('is-active')
        $('#' + $(this).data('target')).toggleClass('is-active')
    })
})