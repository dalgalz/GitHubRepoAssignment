var HOUR = 8;
var MINUTE = 50;
var PERIOD = "AM";

var periodTime;
var dayNightTime;

if( MINUTE == 30)
{
  periodTime = "half past"
}
else if( MINUTE < 30 )
{
  if( MINUTE == 15 )
  {
    periodTime = "quarter after"
  }
  else
  {
    periodTime = "just after"
  }
}
else if( MINUTE > 30 )
{
  if( MINUTE == 45)
  {
    periodTime = "quarter to"
  }
  else
  {
    periodTime = "almost"
  }
  HOUR += 1;
}

if( PERIOD == "AM" )
{
  dayNightTime = "in the morning"
}
else if( PERIOD == "PM")
{
  dayNightTime = "at night"
}

console.log("It's " + periodTime + " " + HOUR + " " + dayNightTime );
