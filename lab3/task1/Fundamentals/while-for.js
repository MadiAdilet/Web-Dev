let i = 3;

while (i) {
  alert( i-- );
} // shows 1 as last





let i = 0;
while (++i < 5) alert( i );
//shows from 1 to 4

let i = 0;
while (i++ < 5) alert( i );
//shows from 0 to 4





for (let i = 0; i < 5; i++) alert( i );
for (let i = 0; i < 5; ++i) alert( i );

//both will show from 0 to 4





for(int i = 2; i <= 10; i+=2){
    alert(i);
}






let i = 0;
while(i < 3){
    alert(`number ${i++}`);
}







let num;

do {
  num = prompt("Enter a number greater than 100?", 0);
} while (num <= 100 && num);








let n = 10;

nextPrime:
for (let i = 2; i <= n; i++) { 

  for (let j = 2; j < i; j++) { 
    if (i % j == 0) continue nextPrime; 
  }

  alert(i); 
}