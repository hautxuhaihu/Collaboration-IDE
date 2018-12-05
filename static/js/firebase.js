function init() {

        setInterval(getMessages, 5000, response["id"]);

        var config = {
            apiKey: "AIzaSyBI8uzW2FaBTe_NCceJbgFsNxcz_EeBOUw",
            authDomain: "collabide-2350f.firebaseapp.com",
            databaseURL: "https://collabide-2350f.firebaseio.com"
        };
        firebase.initializeApp(config);
        //// Get Firebase Database reference.
        var firepadRef = getExampleRef();
        //// Create ACE
        var editor = ace.edit("firepad-container");
         var value = document.getElementById("theme").value;

        console.log(value);
        editor.setTheme("ace/theme/" + value);

        var session = editor.getSession();
        session.setUseWrapMode(true);
        session.setUseWorker(false);
         var value = document.getElementById("language").value;

        console.log(value);
        session.setMode("ace/mode/" + value);
        //// Create Firepad.
        var firepad = Firepad.fromACE(firepadRef, editor, {
            defaultText: ''
        });
    }
    // Helper to get hash from end of URL or generate a random one.
    function getExampleRef() {
        var ref = firebase.database().ref();
        window.location.hash = response["hashvalue"];
        var hash = window.location.hash.replace(/#/g, '');

        if (hash) {
            ref = ref.child(hash);
        } else {
            ref = ref.push(); // generate unique location.
            window.location = window.location + '#' + ref.key; // add it as a hash to the URL.
        }
        if (typeof console !== 'undefined') {
            console.log('Firebase data: ', ref.toString());
        }
        return ref;
    }
