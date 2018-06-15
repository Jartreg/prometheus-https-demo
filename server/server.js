const http = require("http");
const https = require("https");

const fs = require("fs");
const path = require("path");

const app = require("./app");

// HTTP Server
http.createServer(app).listen(80);

// HTTPS Server
const options = {
  key: fs.readFileSync(path.resolve(__dirname, "../certificates/site/site.key.pem")),
  cert: fs.readFileSync(path.resolve(__dirname, "../certificates/site/site.cert.pem"))
};

https.createServer(options, app).listen(443);