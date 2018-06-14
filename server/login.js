const users = new Map();

const usersJson = require("./users");
for(const name in usersJson) {
    users.set(name, usersJson[name]);
}

function checkPassword(user, password) {
    if(typeof user !== "string" || typeof password !== "string")
        return false;

    return users.get(user) === password;
}

module.exports = {
    checkPassword
};