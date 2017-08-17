var luckyNum = 53;
var quarterNum = 40;
var expectedCoins = 200;


while( quarterNum > 0 && quarterNum != 200)
{
  quarterNum--;
  if(playSlot(quarterNum))
  {
      quarterNum = getWinningCoin(quarterNum);
      console.log( "You current coins: " + quarterNum);
  }
}

function playSlot(quarterNum)
{
  console.log( "You coins: " + quarterNum);
  var randomWin = Math.floor( Math.random() * 100 ) + 1;
  return randomWin == luckyNum;
}

function getWinningCoin(coin)
{
  var coinWin = Math.floor( Math.random() * 51 ) + 50;
  console.log("You win " + coinWin + " coins.");
  quarterNum += coinWin;
  return quarterNum;
}
