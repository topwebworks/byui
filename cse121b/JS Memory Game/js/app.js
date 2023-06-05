// TODO: Declare a variable "cards", which is an array that holds all elements with class "card"
// Hint: Use getElementsByClassName()
let card = document.getElementsByClassName("card");
let cards = [...card];

// deck of all cards in game
const deck = document.getElementById("card-deck");

// TODO: Declare a variable "move" that will hold a number value for the number of moves made
let move = 0;

// TODO: Declare a variable "counter" that will hold the element with class "moves"
// Hint: Use querySelector()
let counter = document.querySelector(".moves");

// declaring variable of matchedCards
let matchedCard = document.getElementsByClassName("match");

// TODO: Declare a variable "openedCards" as an empty array
let openedCards = [];

// TODO: Declare variables "second" and "minute" that hold a number value for seconds/minutes elapsed
let second = 0;
let minute = 0;

// TODO: Declare variable "timer" that will hold the element with class "timer"
// Hint: Use querySelector()
let timer = document.querySelector(".timer");

// Use this variable for assigning the setInterval()
var interval;

// @description shuffles cards
// @param {array}
// @returns shuffledarray
function shuffle(array) {
	var currentIndex = array.length,
		temporaryValue,
		randomIndex;

	while (currentIndex !== 0) {
		randomIndex = Math.floor(Math.random() * currentIndex);
		currentIndex -= 1;
		temporaryValue = array[currentIndex];
		array[currentIndex] = array[randomIndex];
		array[randomIndex] = temporaryValue;
	}

	return array;
}

// @description reset/initialize the game when page is refreshed / loads
document.body.onload = startGame();

// @description function to start a new play
function startGame() {
	// empty the openCards array
	openedCards = [];

	// shuffle deck
	cards = shuffle(cards);

	for (var i = 0; i < cards.length; i++) {
		const card = cards[i];
		// TODO: Reset "deck" innerHTML
		deck.innerHTML = "";

		// TODO: Append each "card" (from cards array) to the "deck" element
		cards.forEach.call(cards, function (card) {
			deck.appendChild(card);
		});

		// remove dynamic classes from card
		card.classList.remove("show", "open", "match", "disabled");
	}

	// TODO: Reset the moves counter and value displayed in HTML
	move = 0;
	counter.innerHTML = move;

	// TODO: Reset the timer counter variables: second, minute
	let second = 0;
	let minute = 0;
	// let hour = 0;

	// TODO: Set the innerHTML for the "timer" element to display starting time
	timer.innerHTML = "0 mins 0 secs";
	timer.innerHTML = `${minute} mins ${second} secs`;

	// TODO: Stop the "interval" timer
	clearInterval(interval);
}

// @description toggles open and show class to display cards
var displayCard = function () {
	this.classList.toggle("open");
	this.classList.toggle("show");
	this.classList.toggle("disabled");
};

// @description add opened cards to OpenedCards list and check if cards are match or not
function cardOpen() {
	const selectedCard = this;

	// TODO: Append "selectedCard" to the "openedCards" array
	openedCards.push(selectedCard);

	// TODO: Add conditional to check if 2 cards are "open"
	if (openedCards.length === 2) {
		// TODO: Increment the number of "moves" and start the "timer" if it was the first move
		move++;
		counter.innerHTML = move;
		if (move == 1) {
			second = 0;
			minute = 0;
			hour = 0;
			startTimer();
		}
		// TODO: Call matched() or unmatched() depending on whether both cards have the same "type" attribute
		if (openedCards[0].type === openedCards[1].type) {
			matched();
		} else {
			unmatched();
		}
	}
}

// @description when cards match
function matched() {
	openedCards[0].classList.add("match", "disabled");
	openedCards[1].classList.add("match", "disabled");
	openedCards[0].classList.remove("show", "open", "no-event");
	openedCards[1].classList.remove("show", "open", "no-event");
	openedCards = [];
}

// description when cards don't match
function unmatched() {
	openedCards[0].classList.add("unmatched");
	openedCards[1].classList.add("unmatched");
	disable();
	setTimeout(function () {
		openedCards[0].classList.remove("show", "open", "no-event", "unmatched");
		openedCards[1].classList.remove("show", "open", "no-event", "unmatched");
		enable();
		openedCards = [];
	}, 1100);
}

// @description disable cards temporarily
function disable() {
	Array.prototype.filter.call(cards, function (card) {
		card.classList.add("disabled");
	});
}

// @description enable cards and disable matched cards
function enable() {
	Array.prototype.filter.call(cards, function (card) {
		card.classList.remove("disabled");
		for (var i = 0; i < matchedCard.length; i++) {
			matchedCard[i].classList.add("disabled");
		}
	});
}

// @description game timer
function startTimer() {
	interval = setInterval(function () {
		timer.innerHTML = minute + " mins " + second + " secs";
		second++;
		if (second == 60) {
			minute++;
			second = 0;
		}
		if (minute == 60) {
			hour++;
			minute = 0;
		}
	}, 1000);
}

// @description congratulations when all cards match, show details
function congratulations() {
	if (matchedCard.length == 16) {
		// TODO: Stop the "interval" timer
		// Hint: See clearInterval()
		clearInterval(interval);
		finalTime = timer.innerHTML;

		document.querySelector(".popup").classList.add("show");

		// TODO: Update HTML for element with id "finalMove" to show "moves" value
		let finalMove = document.getElementById("finalMove");
		finalMove.innerHTML = move;

		// TODO: Update HTML for element with id "totalTime" to show innerHTML from "timer" element
		let totalTime = document.getElementById("totalTime");
		totalTime.innerHTML = timer.innerHTML;
	}
}

// @desciption for user to play Again
function playAgain() {
	// TODO: Should call the existing "startGame()" method to start a new game
	startGame();
}

// loop to add event listeners to each card
for (var i = 0; i < cards.length; i++) {
	const card = cards[i];

	// TODO: Add 'click' event listener to call exising "displayCard" method
	card.addEventListener("click", displayCard);

	card.addEventListener("click", cardOpen);
	card.addEventListener("click", congratulations);
}
