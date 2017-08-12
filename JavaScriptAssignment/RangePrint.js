printRange(2, 10, 2);
printRange(4, 8);
printRange(4);

printRange(-10, -2, 3);
printRange(-14, -8);
printRange(12);

function printRange(start, end, increment)
{
  console.log("Start Printing Range...")
  if( increment == undefined)
  {
    increment = 1;
    if( end == undefined)
    {
      end = start;
      start = 0;
    }
  }

  for( var i = start; i < end; i += increment)
  {
    console.log(i);
  }
}
