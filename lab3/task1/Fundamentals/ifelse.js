if ("0") {
    alert( 'Hello' );
  }
  // Yes, because "0" is a string, so it is true






  let name = promt("What is the official name of JavaScript?", "");

if(name == "ECMAScript"){
    alert("Right!");
} else {
    alert("You don't know? ECMAScript!");
}






let num = prompt("Enter a number?", "");
if(num > 0) {
    alert("1")
} else if(num < 0) {
    alert("-1")
} else {
    alert("0")
}






let result = (a + b < 4) ? 'Below' : "Over";







let message = (login == 'Employee') ? 'Hello' :
  (login == 'Director') ? 'Greetings' :
  (login == '') ? 'No login' :
  '';