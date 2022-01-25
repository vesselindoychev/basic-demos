function fishTank(input){
    let length = Number(input[0]);
    let width = Number(input[1]);
    let height = Number(input[2]);
    let percent = parseFloat(input[3]);
    let aquariumVolume = length * width * height;
    let totalWaterVolume = aquariumVolume * 0.001;
    let percentWater = percent * 0.01;
    let waterTank = totalWaterVolume * (1 - percentWater);

    console.log(waterTank);
}
fishTank(["85", "75", "47", "17"]);