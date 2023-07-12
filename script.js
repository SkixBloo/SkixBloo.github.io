const request = new XMLHttpRequest();
request.open("GET", "https://api.scratch.mit.edu/users/BluShuMon/followers");
request.send();
request.onload = () => {
  if(request.status === 200) {
    console.log(JOSN.parse(request.response));
  } else {
    console.log(request)
    console.log(`error${request.status}`)
