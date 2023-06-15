document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    var form = document.getElementById("loginForm");
    var formData = new FormData(form);

    fetch("https://music-sharing-portal.onrender.com/api/accounts/register/", {
      method: "POST",
      body: formData,
    })
      .then(function (response) {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error("Error: " + response.status);
        }
      })
      .then(function (data) {
        console.log(data); // Handle the response data
      })
      .catch(function (error) {
        console.error(error); // Handle any errors
      });
  });
