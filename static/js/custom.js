$('.modal-button').on('click', function () {
    var title_tag = "name-"+$(this).val();

    //console.log(title_tag);
    var description_tag = "description-"+$(this).val();

    $("#modal-titler").html(document.getElementById(title_tag).textContent);
    $("#modal-description").html(document.getElementById(description_tag).textContent);

    console.log("hello ji");
});

function Validate() {

    var title = document.forms["createproject"]["createtitle"].value;

    console.log("dlndnf");

    if(title === "") {
        alert('Title is mandatory');
        return false;
    }

    return true;
}