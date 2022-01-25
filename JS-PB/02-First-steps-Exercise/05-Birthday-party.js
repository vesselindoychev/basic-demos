function birthdayParty(input){
    let rentHall = Number(input[0]);
    let cake = rentHall * 0.2;
    let drinks = cake - ((45 / 100) * cake);
    let animator = rentHall / 3;
    let totalPrice = rentHall + cake + drinks + animator;
    console.log(totalPrice);
}
birthdayParty(["2250"]);