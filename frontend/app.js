const API = "http://127.0.0.1:8000/api/";
const TOKEN = "PASTE_YOUR_JWT_TOKEN_HERE";

function createPost() {
  const content = document.getElementById("content").value;

  fetch(API + "posts/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + TOKEN
    },
    body: JSON.stringify({ content })
  }).then(loadFeed);
}

function loadFeed() {
  fetch(API + "feed/", {
    headers: {
      "Authorization": "Bearer " + TOKEN
    }
  })
  .then(res => res.json())
  .then(data => {
    const feed = document.getElementById("feed");
    feed.innerHTML = "";
    data.forEach(post => {
      feed.innerHTML += `
        <div class="post">
          <strong>${post.user}</strong>
          <p>${post.content}</p>
        </div>
      `;
    });
  });
}

loadFeed();
