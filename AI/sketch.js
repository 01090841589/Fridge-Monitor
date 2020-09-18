// Your code will go here
// open up your console - if everything loaded properly you should see 0.3.0
console.log('ml5 version:', ml5.version);


let classify;
let img;

img = document.getElementById("photo");
classify = ml5.imageClassifier("MobileNet", modelReady);
console.log(classify)
function modelReady() {
  classify.classify(img, gotResults);
}

function gotResults(error, results) {
  if (error) {
    alert(error);
  } else {
    console.log(results);
    document.getElementById("results").innerText =
      "결과 : " +
      results[0].label +
      " 신뢰도 : " +
      String(results[0].confidence);
  }
}