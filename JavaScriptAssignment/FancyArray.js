var arr = ["James", "Jills", "Jane", "Jack"];

printArray(arr, "=>", false);
printArray(arr, "---->", true)

function printArray( array, arrow, isReverse)
{
  if(!isReverse)
  {
    console.log("Printing orderly...");
    for(var i = 0; i < array.length; i++)
    {
      console.log( i + " " + arrow + " " + array[i]);
    }
  }
  else
  {
    console.log("Printing reversing order...")
    for(var i = array.length-1; i >= 0; i--)
    {
      console.log( i + " " + arrow + " " + array[i]);
    }
  }
}
