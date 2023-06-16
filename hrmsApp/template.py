OTP_AUTHENTICATOIN_MAIL_TEMPLATE = """
<!DOCTYPE html>
<html>
    <head>
        <title>One-Time Password</title>
        <meta charset="UTF-8">
        <style>
            body {
                font-family: "Segoe UI Emoji", Arial, sans-serif;
                /* background-color: #eaf2f8; */
                background-color: #FFFFFF;
            }
            table {
                width: 600px;
                background-color: #389197;
                color:#ffffff;
                border-radius:7px;
                font-family: "Segoe UI Emoji", Arial, sans-serif;
                font-size:22px;
                font-weight:400;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            }
              td {
                padding-left:15px;
                padding-right:25px;
                padding-top:1px;
                padding-bottom:1px;
                line-height:140%;
              }

              #otp{
                background-color: #4CAF50;
                width:auto;
                font-weight:600;
                font-size:26px;
                padding:10px;
                border-radius:5px;
                font-family: Arial, Helvetica, Verdana, Tahoma, sans-serif;

              }
              #title{
                font-size:35px;
                font-weight:600;
                padding-top:10px;
              }
              #last{
                padding-bottom:20px;
              }
              #message{
                font-size:21px;
              }  
              .data{
                  padding-left:20px;
                  margin-top:10px;
              }
              .container{
                  height:auto;
                  width:600px;
                  background-color:#38919;
                  border-radius:5px;
                  box-shadow: 0 2px 5px rgba(20, 30, 40, 50);
              }
              @media screen and (max-width: 480px) {
                /* Adjust styles for smaller screens */
                td {
                  display: block;
                  width: 100%;
                  box-sizing: border-box;
                  border: none;
                  padding-left:15px;
                  margin-bottom: 10px;
                }
              }
              @media screen and (max-width: 375px) {
                /* Adjust styles for smaller screens */
                td {
                  display: block;
                  width: 100%;
                  box-sizing: border-box;
                  border: none;
                  padding-left:10px;
                  margin-bottom: 10px;
                }
              }
        </style>
    </head>
    <body>
        <span class="container">
        <table>
            <tbody>
                <tr> <td id="title"> <div class="data"> One-Time Password </div> </td> </tr>
                <tr> <td> <div class="data">Dean Sankian  ,</div> </td> </tr>
                <tr> <td> <div class="data">Your one-time password (OTP) is : </div></td> </tr> 
                <tr> <td> <div class="data"><span id="otp"> mail_otp </span> </td> </tr>
                <tr> <td id="message"><div class="data"> Please use this OTP to complete your login or verification process. Please note that this code will expire in 60 seconds for security purposes. </div> </td> </tr>
                <tr> <td><div class="data"> Best regards, </div> </td> </tr>
                <tr> <td id="last"> <div class="data">HR & Financial Team </div> </td> </tr>
            </tbody>
        </table>
        </span>
    </body>
</html>
"""