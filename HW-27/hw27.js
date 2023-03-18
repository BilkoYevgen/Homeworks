//  Додати на раніше створену сторінку кнопки “Додати в друзі”, “Написати повідомлення”, “Запропонувати роботу”.
let sendMessageBtn = document.createElement("button");
sendMessageBtn.innerHTML = "Написати повідомлення";
sendMessageBtn.style.background = "purple"
sendMessageBtn.addEventListener("click", function () {
    alert("Напишіть своє повідомлення тут.");
});
document.body.appendChild(sendMessageBtn);


let jobOfferBtn = document.createElement("button");
jobOfferBtn.innerHTML = "Запропонувати роботу";
jobOfferBtn.style.background = "purple"
jobOfferBtn.addEventListener("click", function () {
    alert("Відкривається форма для заповнення пропозиції роботи.");
});
document.body.appendChild(jobOfferBtn);

// 2. Додати окремий елемент, що має відображати кількість друзів. Ця кількість має ініціалізуватися як рандомне число при завантаженні сторінки, а при натисканні на "Додати в друзі" збільшуватися на 1.
// Зробити неможливим повторне натискання кнопки “Додати в друзі”, змінювати її назву на “Очікується підтвердження” одразу після натискання і робити неактивною.

let friendCount = Math.floor(Math.random() * 100) + 1;

let addFriendBtn = document.getElementById("addFriendBtn");
let friendCountSpan = document.getElementById("friendCount");

friendCountSpan.innerHTML = friendCount + " друзів";

addFriendBtn.addEventListener("click", function () {

    addFriendBtn.disabled = true;

    addFriendBtn.innerHTML = "Очікується підтвердження";
    addFriendBtn.style.backgroundColor = "gray";
    addFriendBtn.style.color = "white";

    friendCount++;
    friendCountSpan.innerHTML = friendCount + " друзів";
});