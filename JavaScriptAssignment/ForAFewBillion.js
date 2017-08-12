var totalMoney = 0;

for( var i = 0; i < 30; i++)
{
  totalMoney += (0.01*(Math.pow(2,i)));
}

console.log( "The servant would get a total of: " + totalMoney + " on 30th day.")
totalMoney = 0;

for(var i = 0;; i++)
{
  totalMoney += (0.01*(Math.pow(2,i)));
  if(totalMoney >= 10000)
  {
    console.log("The servant would got 10,000 in " + (i + 1) + " days")
    break;
  }
}
totalMoney = 0;

for(var i = 0;; i++)
{
  totalMoney += (0.01*(Math.pow(2,i)));
  if(totalMoney >= 1000000000)
  {
    console.log("The servant would got a billion in " + (i + 1) + " days")
    break;
  }
}
totalMoney = 0;

for(var i = 0;; i++)
{
  totalMoney += (0.01*(Math.pow(2,i)));
  if(totalMoney >= Infinity)
  {
    console.log("The servant would got Maximum Number of " + totalMoney +" in " + (i + 1) + " days")
    break;
  }
}
