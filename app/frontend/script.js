const button = document.getElementById("generate");

button.addEventListener("click", async () => {
  console.log("clicked");
  const topic = document.getElementById("topic").value;
  document.getElementById("summary").innerText = "Generating summary...";
  try {
    document.getElementById("loading").classList.remove("hidden");
    button.disabled = true;
    const response = await fetch(
      `http://127.0.0.1:8000/news-summary?topic=${topic}`,
    );
    const data = await response.json();
    button.disabled = false;
    document.getElementById("summary").innerText = data.summary;
  } catch (error) {
    document.getElementById("summary").innerText = "Something went wrong";
  } finally {
    document.getElementById("loading").classList.add("hidden");
  }
});
