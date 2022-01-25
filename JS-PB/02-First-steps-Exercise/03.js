function depositCalculator(input){
    let depositSum = parseFloat(input[0]);
    let deadLine = Number(input[1]);
    let anualPercentage = parseFloat(input[2]);
    let res = depositSum + deadLine * (((depositSum * anualPercentage) / 100) / 12);
    console.log(res);
}
depositCalculator(["2350", "6", "7"])