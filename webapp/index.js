var db = firebase.database();
var ref = db.ref('last_update');



ref.on('value', function(snapshot){
    console.log(snapshot.val());
    var status = snapshot.val().status;
    var time = snapshot.val().time;

    document.getElementById("status").textContent= status;

    document.getElementById("time_S").textContent = time;
})