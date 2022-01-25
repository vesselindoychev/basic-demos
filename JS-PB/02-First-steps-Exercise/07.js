function fruitMarket(input){
    let strawberryPrice = parseFloat(input[0]);
    let bananasKg = parseFloat(input[1]);
    let orangesKg = parseFloat(input[2]);
    let berryKg = parseFloat(input[3]);
    let strawberryKg = parseFloat(input[4]);
    let berryPrice = strawberryPrice / 2;
    let orangeaPrice = berryPrice * 0.6;
    let banansPrice = berryPrice * 0.2;

    let strawberrySum = strawberryPrice * strawberryKg;
    let banansSum = banansPrice * bananasKg;
    let orangesSum = orangeaPrice * orangesKg;
    let berrySum = berryPrice * berryKg;

    let totalSum = strawberrySum + berrySum + banansSum + orangesSum;
    console.log(totalSum);
}
fruitMarket(["48", "10", "3.3", "6.5", "1.7"]);
fruitMarket(["63.5", "3.57", "6.35", "8.15", "2.5"])