/* 
  Given two arrays, interleave them into one new array.
  The arrays may be different lengths. The extra items should be added to the
  back of the new array.
*/

const arrA1 = [1, 2, 3];
const arrB1 = ["a", "b", "c"];
const expected1 = [1, "a", 2, "b", 3, "c"];

const arrA2 = [1, 3];
const arrB2 = [2, 4, 6, 8];
const expected2 = [1, 2, 3, 4, 6, 8];

const arrA3 = [1, 3, 5, 7];
const arrB3 = [2, 4];
const expected3 = [1, 2, 3, 4, 5, 7];

const arrA4 = [];
const arrB4 = [42, 0, 6];
const expected4 = [42, 0, 6];

/**
 * Interleaves two arrays into a new array. Interleaving means alternating
 * the items starting from the first array.
 * - Time: O(?).
 * - Space: O(?).
 */
function interleaveArrays(arr1, arr2) {
    var newarr = []

        for(var a = 0; a < arr1.length+arr2.length; a++){
        
            if(a < arr1.length){
                    newarr.push(arr1[a])
                }
            if(a < arr2.length){
                newarr.push(arr2[a])
            }
        }

            
                
        
    return newarr
}

console.log(interleaveArrays(arrA4,arrB4))