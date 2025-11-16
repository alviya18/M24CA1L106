const cards = document.querySelectorAll(".card");
const playerBar = document.getElementById("playerBar");
const globalAudio = document.getElementById("globalAudio");
const playerInfo = document.getElementById("playerInfo");
const closePlayer = document.getElementById("closePlayer");

let currentCard = null;   // currently highlighted card
let currentSoundId = null; // currently playing sound ID

function showPlayer(name, url) {
  // playerInfo.textContent = name;
  globalAudio.src = url;
  globalAudio.play();
  playerBar.hidden = false;
}

function hidePlayer() {
  globalAudio.pause();
  globalAudio.src = "";
  playerBar.hidden = true;
  if (currentCard) {
    currentCard.classList.remove("playing");
    currentCard = null;
    currentSoundId = null;
  }
}

cards.forEach((card) => {
  const playBtn = card.querySelector(".play-btn");
  const stopBtn = card.querySelector(".stop-btn");
  const name = card.querySelector(".label").textContent;
  const url = card.dataset.soundUrl;
  const sid = card.dataset.soundId;

  playBtn.addEventListener("click", () => {
    if (currentSoundId === sid) {
      // already playing, just resume
      globalAudio.play();
    } else {
      // stop previous card
      if (currentCard) currentCard.classList.remove("playing");

      currentCard = card;
      currentSoundId = sid;

      card.classList.add("playing");
      showPlayer(name, url);
    }
  });

  stopBtn.addEventListener("click", () => {
    if (currentSoundId === sid) {
      hidePlayer();
    }
  });
});

