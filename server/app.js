const express = require("express");
const consolidate = require("consolidate");
const session = require("express-session");
const path = require("path");

const app = express();

app.engine("html", consolidate.dust);
app.set("view engine", "html");
app.set("views", path.resolve(__dirname, "views"));

app.use(session({
    secret: "Tastaturkatze",
    saveUninitialized: false,
    resave: false
}));

// Assets
app.use("/public", express.static(path.resolve(__dirname, "public")));

// Material Design Assets
const mdlJS = require.resolve("material-design-lite/material.min.js");
const mdlCSS = require.resolve("material-design-lite/material.min.css");

app.get("/public/mdl/material.min.js", (req, res) => res.sendFile(mdlJS));
app.get("/public/mdl/material.min.css", (req, res) => res.sendFile(mdlCSS));

app.use((req, res, next) => {
    req.user = req.session ? req.session.user : undefined;
    next();
});

// routes

app.get("/", (req, res) => {
    res.render("index", {
        user: req.user
    });
});

app.get("/login", (req, res) => {
    if (req.user) {
        res.redirect("/");
    } else {
        res.render("login");
    }
});

app.get("/logout", (req, res) => {
    req.session.destroy();
    res.redirect("/");
});

// API

app.post("/api/login", express.json(), (req, res) => {
    if(req.user) {
        res.json({
            success: false,
            message: "Du bist bereits angemeldet."
        });
    } else if (typeof req.body.user === "string" && typeof req.body.password === "string") {
        const user = req.body.user.trim();

        // for demonstration purposes: always log in
        req.session.user = user; // log in
        req.session.save();

        // send successful response
        res.json({
            success: true,
            user
        });
    } else {
        res.sendStatus(400); // Bad Request
    }
});

module.exports = app;