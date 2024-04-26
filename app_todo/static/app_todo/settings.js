const value = document.querySelector("#value");
const input = document.querySelector("#mission_time");
value.textContent = input.value;
input.addEventListener("input", (event) => {
  value.textContent = event.target.value;
});

function startTime() {
  const today = new Date();
  let h = today.getHours();
  let m = today.getMinutes();
  let s = today.getSeconds();
  let mo = today.getMonth();
  let ye = today.getFullYear();
  let da = today.getUTCDate();
  mo = checkMonth(mo);
  m = checkTime(m);
  s = checkTime(s);
  h = checkTime(h);
  document.getElementById('time').innerHTML =  h + ":" + m + ":" + s;
  setTimeout(startTime, 1000);
  document.getElementById('date').innerHTML = da + '  ' + mo + '  ' + ye
}

function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}

function checkMonth(mo) {
  
  month_list = ['January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December']
  return month_list[mo] 
}

