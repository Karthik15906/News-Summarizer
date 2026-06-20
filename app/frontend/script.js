const button = document.getElementById("generate");

button.addEventListener("click", async () => {
  console.log("clicked");
  const topic = document.getElementById("topic").value;
  document.getElementById("summary").innerText = "Generating summary...";
  try {
    button.disabled = true;
    const response = await fetch(
      `http://127.0.0.1:8000/news-summary?topic=${topic}`,
    );
    const data = await response.json();
    document.getElementById("summary").innerText = data.summary;
    button.disabled = false;
  } catch (error) {
    document.getElementById("summary").innerText = "Something went wrong";
  }
});
