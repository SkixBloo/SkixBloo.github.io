fetch('GET https://api.scratch.mit.edu/users/BluShuMon/following', {
  method: 'POST',
  headers: {
    'content-type': 'application/json'
  },
  body: JSON.stringify
  name: 'BluShuMon'
})
}).then(res => {
  return res.json()
})
.then(data => console.log(data))
.catch(error => console.log('ERROR'))
