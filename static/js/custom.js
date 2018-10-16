$('.modal-button').on('click', function () {
    var title_tag = "name-"+$(this).val();

    console.log(title_tag);
    var description_tag = "description-"+$(this).val();
    $("#modal-name").html(document.getElementById(title_tag).textContent);
    $("#modal-description").html(document.getElementById(description_tag).textContent);

    console.log("hello ji");
});

function validateform() {

    var title = document.getElementById('createtitle');

    if(title==='')
        alert('Title is mandatory');

    return false;

}