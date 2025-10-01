

getUser = () => {
  // .value is the thing typed in
  const user = document.getElementById("Username").value;
  const tag = document.getElementById("Tag").value;

  const loading = document.getElementById("load-thing");
  loading.classList.add("load-thing-class");
  loading.textContent = "Loading...";
  document.body.appendChild(loading);

  fetch("http://127.0.0.1:5000/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      Username: user,
      Tag: tag,
    }),
  })

  
  
    // response is just a variable holding the built in response object
    .then((response) => response.json())
    .then((data) => {
      

      console.log(data);
      const champions = data.player.map(function (slop) {
        return slop;
      });

      console.log(champions);
      document.body.removeChild(loading);
      let showChamps = document.getElementById("lists");

      const summary = document.createElement("p");
      summary.classList.add("summary");

      summary.textContent = `Best KDA: ${data.summary["Best KDA"]}  (${data.summary["Best KDA Champion"]})\n
      Worst KDA: ${data.summary["Worst KDA"]} (${data.summary["Worst KDA Champion"]})\n
      Most Used: ${data.summary["Most Used Champion"]}`;
      document.body.appendChild(summary);

      champions.forEach(function (slop2) {
        const game = document.createElement("li");
        const champimage = document.createElement("img");
        const layers = document.createElement("div");

        champimage.classList.add("champ-pic");
        layers.classList.add("layer");
        game.classList.add("stats-text");
        champimage.src = slop2.ChampionPic;
        game.appendChild(champimage);
        game.appendChild(
          document.createTextNode(
            `Champion: ${slop2.Champion}, Kills: ${slop2.Kills}, Deaths: ${slop2.Deaths}, Assists: ${slop2.Assists}, KDA: ${slop2.KDA}, Win: ${slop2.Win}`
          )
        );
        game.appendChild(layers);
        showChamps.appendChild(game);
      });
    })

    .catch((err) => console.error(err));
};
