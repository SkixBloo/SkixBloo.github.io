function getIcon(response){ // ga.js and username
  var obj = JSON.parse(response);
  var src= 'https://cdn2.scratch.mit.edu/get_image/user/'96952848'_60x60.png';
  document.getElementById('icon').src = src;
  document.getElementById('user').innerHTML =  obj.username;
  username = obj.username;
  shouldrefresh = 0;
  /*location.hash = username;*/
  ga('set', 'page', '/user/#'+obj.username);
  ga('send', 'pageview');
}
