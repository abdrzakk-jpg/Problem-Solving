/*

*Explaintaion:
----------------

Write a function that takes an integer as input, 
and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

?- Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case



*Simply: Take Input -> Convert It To Binary-system -> calc how-many-ones are in previous Bin-number:
*like 123 === 1111011, there is: 6-ones 

*/

// #include <stdio.h>


// void CountBits(unsigned int arg, int *counter){
//     //* change to Binary by recuresive devision Then Save 1-bit on the  `counter-var` memory-address 

//     int bi = arg % 2; // The remainder of the division of arg-number
//     int i = 0; // ones-counter

//     while (arg != 0){ // recuresive devision 

//         bi = arg % 2; // reminder of current n
//         arg = arg / 2; // divide by the Base of `2`
        
//         // if remainder is 1
//         if (bi == 1) i ++;
//     }
//     *counter = i;
// }

// int main() {
//     int counter;
//     int *counter_ptr = &counter;
//     unsigned int arg;

//     while (1) {
//         // read arg
//         printf(">>");
//         scanf("%d", &arg);
//         CountBits(arg, counter_ptr);
//         printf("There is [%d]bits in [%d]\n", *counter_ptr, arg);
//     }

//     return 0;
// }

//! Submitted Code :
#include <stddef.h>
size_t countBits(unsigned int value)
{
    int bit_val = value % 2;
    int i = 0;
    while (value != 0){
        bit_val = value % 2; 
        value = value / 2;
        if (bit_val == 1) i ++;
    }

    return i;
}

//* Solved ! *//