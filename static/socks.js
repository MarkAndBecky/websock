$(function() {
    console.log('load');
    $('#units').change(function() {
        $(this).parents('form').submit();
    });


    $('#generate-button').on('click', function(evt) {
        console.log('submitting');
        var form = $(this).parents('form').get(0).setAttribute('action', '/pattern');
        form.submit();

        return false;
    });
});