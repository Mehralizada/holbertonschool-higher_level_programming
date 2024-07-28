async function fr_salut () {
    const saludar = await (await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")).json();
    document.querySelector("#hello").innerHTML = saludar["hello"];
}
fr_salut ()
