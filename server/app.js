const express = require("express");
const path = require("path");

const app = express();

app.use("/public", express.static(path.resolve(__dirname, "public")));

app.get("/", (req, res) => {
    res.send("Hallo");
});

module.exports = app;