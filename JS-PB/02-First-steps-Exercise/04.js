function vacationBooks(input){
    let pagesNumber = Number(input[0]);
    let pagesInOneHours = Number(input[1]);
    let daysNumber = Number(input[2]);
    let totalTime = pagesNumber / pagesInOneHours;
    let res = totalTime / daysNumber;
    console.log(res);
}
vacationBooks(["212", "20", "2"]);