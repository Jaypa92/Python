/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

//bonus
const str5 = "aaabbccdddaaaaa"
const expected5 = "a3b2c2d3a5"

function str_amt(str) {
    var amt = []
    var count = 0
    for (var i = 0; i < str.length; i++) {
        if (str[i] == str[i + 1]) {
            count = count + 1
        }
        else {
            count += 1
            amt.push(str[i])
            amt.push(count)
            count = 0
        }
    }
    result = amt.join("")
    if (result.length < str.length) {
        return result
    }
    else {
        return str
    }
}

console.log(str_amt(str5))







/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs. Only encode strings
 * when the result yields a shorter length.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */
function encodeStr(str) { }
