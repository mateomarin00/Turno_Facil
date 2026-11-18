async function generarTurno() {

    try {

        const respuesta = await fetch(
            "/api/turno",
            {
                method: "POST"
            }
        );

        const datos = await respuesta.json();

        localStorage.setItem(
            "turnoActual",
            JSON.stringify(datos)
        );

        window.location.href =
            "/turno-emitido";

    } catch (error) {

        console.error(error);

    }

}


function mostrarPrioridades() {

    const panel =
        document.getElementById(
            "prioridades"
        );

    panel.style.display = "block";

}


async function generarPrioritario(
    condicion
) {

    const respuesta = await fetch(
        "/api/turno-prioritario",
        {
            method: "POST",
            headers: {
                "Content-Type":
                    "application/json"
            },
            body: JSON.stringify({
                condicion
            })
        }
    );

    const datos = await respuesta.json();

    localStorage.setItem(
        "turnoActual",
        JSON.stringify(datos)
    );

    window.location.href =
        "/turno-emitido";

}