'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  AUTH_URL: '"http://localhost:5000/auth"',
  API_URL: '"http://localhost:5000/api/v1"',
  ROOT_URL: '"http://localhost:5000"'
})
