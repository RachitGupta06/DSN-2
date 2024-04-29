function checkOther(value) {
    var otherLocationInput = document.getElementById("otherLocation");
    if (value === "Other") {
      otherLocationInput.style.display = "inline-block";
      otherLocationInput.required = true;
    } else {
      otherLocationInput.style.display = "none";
      otherLocationInput.required = false;
    }
  }