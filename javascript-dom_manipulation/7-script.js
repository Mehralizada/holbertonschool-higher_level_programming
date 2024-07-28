movies()
async function movies() {
    const response = await (await fetch("https://swapi-api.hbtn.io/api/films/?format=json")).json();
    const movies = response["results"]
    for (title in movies){
        document.querySelector("#list_movies").innerHTML += '<li>' + movies[title]["title"] + '</li>';
    }
  }
