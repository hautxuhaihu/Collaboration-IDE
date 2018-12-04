document.getElementById("theme").addEventListener("change", changeTheme, false);

function changeTheme() {
    var editor = ace.edit("firepad-container");
    var value = document.getElementById("theme").value;

    console.log(value);
    editor.setTheme("ace/theme/" + value);
}

document.getElementById("language").addEventListener("change", changeLanguage, false);

function changeLanguage() {
    var editor = ace.edit("firepad-container");
    var session = editor.getSession();
    session.setUseWrapMode(true);
    session.setUseWorker(false);

    var value = document.getElementById("language").value;

    console.log(value);
    session.setMode("ace/mode/" + value);
}