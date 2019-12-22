var counter = 0

function add_show_file_element(file) {


    var old_file = $("#file").clone();
    old_file.attr('id', 'file_'+counter);
    old_file.attr('name', 'image_file');
    $("#hidden_file").prepend(old_file)

    var div_col_element = $('<div class="col-md-4" id="col_img_'+ counter +'"></div>');
    var thumbnail_element = $('<div class="thumbnail"></div>');
    var a_close_element = $('<a href="#" id="a_close_img_'+ counter +'"></a>');
    a_close_element.append('<i class="fa fa-fw fa-close"></i>');
    var a_image_element = $('<a href="#"></a>');
    a_image_element.append('<img src="'+ file.target.result +'" class="rounded float-left" style="min-height:100px;height:100px;" />');

    thumbnail_element.append(a_close_element);

    thumbnail_element.append(a_image_element);

    div_col_element.append(thumbnail_element);

    a_close_element.click(function() {
        div_col_element.remove();
        old_file.remove();
    });

    $("#show_file").append(div_col_element);
}

function remove_show_file_element() {

}

function readUrl(input) {
    if (input.files && input.files[0]) {
        var render = new FileReader();
        render.onload = function(e) {
            console.log(counter)
            add_show_file_element(e)
            counter = counter + 1
        };
        render.readAsDataURL(input.files[0]);
    }

}

function initialDocument() {
    $("#button_choose").click(function() {
        $("#file").click();
    });

    $("#file").change(function(){
        readUrl(this);
    });

    $("a[name=a_close]").click(function() {
        var id = $(this).data('id');
        console.log(id);
        $(".col-md-4[data-id="+id+"]").remove();
    });
}

$(function() {
    initialDocument()
});