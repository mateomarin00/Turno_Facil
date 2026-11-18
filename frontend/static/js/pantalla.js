async function actualizarPantalla() {

    const respuesta =
        await fetch(
            "/api/pantalla"
        );

    const datos =
        await respuesta.json();

    document.getElementById(
        "turno"
    ).innerText =
        datos.numero;

    document.getElementById(
        "espera"
    ).innerText =
        datos.espera;

    document.getElementById(
        "promedio"
    ).innerText =
        datos.promedio + " min";

}

setInterval(
    actualizarPantalla,
    2000
);

actualizarPantalla();


function actualizarHora(){

    const ahora =
        new Date();

    document
        .getElementById("hora")
        .innerText =
        ahora.toLocaleTimeString();
}

setInterval(
    actualizarHora,
    1000
);

actualizarHora();