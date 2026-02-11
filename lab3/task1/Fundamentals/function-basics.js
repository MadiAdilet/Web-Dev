function checkAge(age) {
    if (age > 18) {
      return true;
    } else {
      // ...
      return confirm('Did parents allow you?');
    }
  }

function checkAge(age) {
    if (age > 18) {
      return true;
    }
    // ...
    return confirm('Did parents allow you?');
  }


//no, cuz return already does the else's function 




function checkAge(age) {
    return (age > 18) ? true : confirm("Did your parents allow you?"); 
  }

function checkAge(age) {
    return (age > 18) || confirm("Did your parents allow you?"); 
  }





  function findmin(a, b){
    if(a < b) return a;
    else return b;
}





function pow(x, n) {
    return x**n;
  }
  
  let x = prompt("x?", '');
  let n = prompt("n?", '');
  
  if (n < 1) {
    alert(`Power ${n} is not supported, use a positive integer`);
  } else {
    alert( pow(x, n) );
  }