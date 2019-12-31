const fs = require('fs');

module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
   devServer: {
    https: {
      key: fs.readFileSync('./certs/localhost-key.pem'),
      cert: fs.readFileSync('./certs/localhost.pem'),
    },
    public: 'https://localhost:8080/'
  }
};