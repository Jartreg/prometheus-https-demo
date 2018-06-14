(() => {
    function login(user, password, success, error) {
        user = user.trim();
        password = password.trim();

        if (!user) {
            error();
            return;
        }

        if (!password) {
            error("Es muss ein Passwort eingegeben werden.");
            return;
        }

        const request = new XMLHttpRequest();
        request.open("POST", "/api/login");
        request.setRequestHeader("Content-Type", "application/json");
        request.responseType = "json";
        request.send(JSON.stringify({
            user,
            password
        }));

        request.addEventListener("error", () => {
            error("Es gab einen Fehler bei der Verbindung.");
        });

        request.addEventListener("load", () => {
            const res = request.response;
            if (res && res.success && typeof res.user === "string") {
                success(res.user);
            } else if (res && typeof res.message === "string") {
                error(res.message);
            } else {
                error("Es gab einen Fehler beim Anmelden.");
            }
        });
    }

    const form = document.getElementById("login-form");
    const user = document.getElementById("user");
    const pw = document.getElementById("password");
    const error = document.getElementById("error");

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        e.disabled = true;
        login(
            user.value,
            pw.value,
            () => {
                location.href = "/";
            },
            (msg) => {
                form.disabled = false;

                if (msg) {
                    error.innerText = msg;
                    error.className = "login-error";
                }
            }
        );
    });
})();