var requestLink ="https://some-random-api.ml/facts/dog"
//get json data from requestLink
var request = new XMLHttpRequest();
request.open('GET', requestLink);
request.responseType = 'json';
request.send();
request.onload = function() {
    var data = request.response;
    console.log(data);
    //get dog facts
    var dogFacts = data.fact;
    document.getElementById("dogFacts").innerHTML = dogFacts;
}
