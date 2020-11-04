// create state.users if it doesn't exist

// ---- IMP ----
//uncomment this to make it work
//state.users = state.users || []

Sandbox.define('/users', 'POST', function(req, res) {
    // validate username is present
    if (req.body.username === undefined) {
      return res.json(400, { status: "error", details: "Missing username" })
    }
  
    state.users.push(req.body)
  
    return res.json({status: "ok"})
  })
  
  Sandbox.define('/users', 'GET', function(req, res) {
    if (req.query.age) {
      // convert req.query.age from String to a Number before comparing
      return res.json(_.filter(state.users, { 'age': Number(req.query.age) }))
    }
  
    return res.json(state.users)
  })
  
  Sandbox.define('/users/{username}', 'GET', function(req, res) {
    var user = _.find(state.users, { 'username': req.params.username })
    
    // respond with 404 if user isn't found
    if (!user) { 
      return res.json(404, { error: { message: 'User doesnt exist check if imp is commented out' } }) 
    }
    
    return res.json(user)
  })
  Sandbox.define('/users/{username}', 'DELETE', function(req, res) {
    var user = _.find(state.users, { 'username': req.params.username })
      
    if (!user) {
        return res.json(404, { error: { mesage: 'User doesnt exist check if imp is commented out'} })
    }
    
    // use Lodash reject to remove the user
    state.users = _.reject(state.users, { 'username': req.params.username })
    
    return res.json({status: 'ok'})
  })
  
  Sandbox.define('/users/{username}', 'PUT', function(req, res) {
    var user = _.find(state.users, { username: req.params.username })
      
    if (!user) { 
      return res.json(404, { error: { message: 'User doesnt exist check if imp is commented out' } }) 
    }
      
    // update the user object
    _.merge(user, req.body)
    
    // drop the user and subsequently readd
    state.users = _.reject(state.users, { username: req.params.username })
    state.users.push(user)
    
    return res.json({ status: 'ok'})
  })