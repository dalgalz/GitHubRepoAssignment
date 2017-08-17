var newArray = numbersOnly([1, "apple", -3, "orange", 0.5]);

function numbersOnly(arr){
  var newArr = [];
  for( var i = 0; i < arr.length; i++ )
  {
    if( typeof arr[i] === "number" )
    {
      newArr.push(arr[i]);
    }
  }
  return newArr;
}

console.log(newArray);

var anotherArray = ["wow", "apple", "glad", "orange", 0.5, "Dan", 7];
sameArrNumOnly(anotherArray);

function sameArrNumOnly(anotherArray)
{
  for( var i = 0; i < anotherArray.length; i++ )
  {
    if( typeof anotherArray[i] !== "number" )
    {
      anotherArray.splice(i, 1);
      i--;
    }
  }
}

console.log(anotherArray);
