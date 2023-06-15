function moveToNext(currentInput, nextInputId) {
    const maxLength = currentInput.getAttribute("maxlength");
    const currentLength = currentInput.value.length;
  
    if (currentLength === maxLength) {
      if (nextInputId !== null) {
        const nextInput = document.getElementById("otp" + nextInputId);
        nextInput.readOnly = false;
        nextInput.focus();
      }
    }
  }
  
  function checkButtonState() {
    const otpInputs = document.getElementsByClassName("otp-input");
    const verifyButton = document.getElementById("verify-btn");
  
    let filledCount = 0;
    let otpValue = "";
    for (let i = 0; i < otpInputs.length; i++) {
      const otpInput = otpInputs[i];
      otpValue += otpInput.value;
  
      if (otpInput.value.length === 1) {
        filledCount++;
      } else {
        break;
      }
    }
  
    if (filledCount === otpInputs.length) {
      verifyButton.disabled = false;
    } else {
      verifyButton.disabled = true;
    }
  
    // Store the combined OTP value
    document.getElementById("otpValue").value = otpValue;
  }
  
  function verifyOTP() {
    const otpValue = document.getElementById("otpValue").value;
  
    // Perform OTP verification or other actions
    console.log("OTP:", otpValue);
  
    // Send OTP value to the backend using AJAX or form submission
    // Example using AJAX with jQuery:
    $.ajax({
         url: "{% url 'verifyOTP' %}",
         method: "POST",
         data: { otp : otpValue },
         success: function(response) {
             // Handle response from the backend
         },
         error: function(error) {
             // Handle error
         }
     }); 
  }
  