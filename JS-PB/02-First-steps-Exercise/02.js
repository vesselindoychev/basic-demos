function radToDeg(input){
    
    let rad = parseFloat(input[0]);
    let deg = rad * 180 / Math.PI;
    console.log(deg.toFixed(0));
}
radToDeg(["3.1416"])