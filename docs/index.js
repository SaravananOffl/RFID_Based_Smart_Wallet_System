var db = firebase.database();
var ref = db.ref('last_update');



ref.on('value', function(snapshot){
//    console.log(snapshot.val());
    var status = snapshot.val().status;
    var time = snapshot.val().time;

    document.getElementById("status").textContent= status;
    document.getElementById("time_S").textContent = time;
    
    
}, function(error){
    console.log("Error is" , error);
    document.getElementById("status").textContent = "error";
    document.getElementById("time_S").textContent = "error";
});


var list = document.getElementById("log");

var refLog = db.ref('wallet_log');
var dataLogList = [];
dataLogList.push("<th>Date</th> <th> Time </th> <th> Status </th>");
refLog.on('value', function(snapshot){

    var dataLog = snapshot.val();
    for (item in dataLog){
        console.log("item is" , item,dataLog[item], '\n' )
        for (element in dataLog[item]){
            var classT ="table-success";
            if((" Wallet is not connected").localeCompare(dataLog[item][element])==0){
                console.log("Done");
                classT = "table-danger";
            }
            dataLogList.push("<tr class="+classT+"><td>"+item+"</td><td>"+element+ "</td>"+"<td>" +dataLog[item][element]+"</td></tr>");
       
        }
    }
    
var clusterize = new Clusterize({
  rows: dataLogList,
  scrollId: 'scrollArea',
  contentId: 'contentArea'
});
});


