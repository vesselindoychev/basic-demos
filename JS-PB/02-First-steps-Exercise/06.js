function charityCampaign(input){
    let days = Number(input[0]);
    let bakersCount = Number(input[1]);
    let cakesCount = Number(input[2]);
    let wafflesCount = Number(input[3]);
    let pancakesCount = Number(input[4]);
    let cakePrice = 45;
    let wafflePrice = 5.80;
    let pancakePrice = 3.20;
    let pricePerDay = (cakesCount * cakePrice + wafflesCount * wafflePrice + pancakesCount * pancakePrice) * bakersCount;
    let totalPrice = pricePerDay * days;
    let finalPrice = totalPrice - totalPrice * 1/8;
    console.log(finalPrice);
}
charityCampaign(["23", "8", "14", "30", "16"]);