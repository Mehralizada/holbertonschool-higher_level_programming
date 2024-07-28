characters()
async function characters() {
    const response = await (await fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")).json();
    document.querySelector("#character").innerHTML = response["name"];
  }
