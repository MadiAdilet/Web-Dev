let a = 1, b = 1;

let c = ++a; // both of them 2
let d = b++; // d = 1, b = 2



let a = 2;

let x = 1 + (a *= 2);

//x = 5, a = 4



let a = 2;

let x = 1 + (a *= 2);

//x = 5, a = 4






"" + 1 + 0
"" - 1 + 0
true + false
6 / "3"
"2" * "3"
4 + 5 + "px"
"$" + 4 + 5
"4" - 2
"4px" - 2
"  -9  " + 5
"  -9  " - 5
null + 1
undefined + 1
" \t \n" - 2

//10, -1, 1, 2, 6, 9px, $45, 2, NaN, -9   5, -14, 1, NaN, -2








let a = prompt("First number?", 1);
let b = prompt("Second number?", 2);

alert(a + b); // 12

// because a and b are strings, so the result is 12
// to fix this, we need to convert a and b to numbers

let a = prompt("First number?", 1);
let b = prompt("Second number?", 2);

alert(Number(a) + Number(b)); // 3

// now the result is 3

