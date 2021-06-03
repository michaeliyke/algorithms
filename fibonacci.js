function fibonacci() {
	let placeholder = foo = 0; 
	let current = 1, array = [];
	return function fib(number){
		current += foo
		array.push(placeholder)
		foo = placeholder
		placeholder = current
		return placeholder < number ? fib(number): array.join(" ");
	};
}

let f = fibonacci();

console.log(f(100))

// current =     [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
// foo = 				 [0, 1, 1, 2, 3, 5, 8,13, 21, 34]
// placeholder = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]