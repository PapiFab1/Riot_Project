getUser = () => {
    // .value is the thing typed in
    const user = document.getElementById("Username").value;
    const tag = document.getElementById("Tag").value;

    // window.location.href = "stats.html";

    fetch("http://127.0.0.1:5000/",{
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            Username: user,
            Tag: tag
        })
    })
    // response is just a variable holding the built in response object
    .then(response => response.json())
    .then(data => {

        console.log(data);
    })
    .catch(err => console.error(err));

}


