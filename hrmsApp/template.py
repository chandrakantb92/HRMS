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

PAY_SLIP_TEMPLATE = """
{% load static %}
<!DOCTYPE html>
<html>
    <head>
<style>
    .slip-wrap {
        border: 3px black solid;
        margin: 30px;
    }
    .border-box{
        border: 2px black solid;
        width: 100%;
        margin-bottom: 20px;
        margin-top: 16px;
    
    }

    .note {
        bottom: 420px;
        position: fixed;
        text-align: center;
    }

    .th {
        border: 1px solid black;
        padding: 4px;
    }

    .table {
        border-collapse: collapse;
        width: 100%;
    }

    .th {
        height: 12px;
    }

    .right {
        text-align: right;
    }

    .left {
        text-align: left;
    }

    .center {
        text-align: center;
    }

    .noborders td {
        border: 1px solid;
    }

    .pl {
        padding-left: 1px;
    }

    .pr {
        padding-right: 2px;
    }

    .bb {
        border-bottom: 1px solid #ffffff;
    }

    .bl {
        border-left: 1px solid #ffffff;
    }

    .br {
        border-right: 1px solid #ffffff;
    }

    .bt {
        border-top: 1px solid #000000;
    }
    .header {
        font-weight: 600;
    }
    .bold-text {
        font-weight: 520;
    }
    .sub-heading {
        font-size: 12;
    }
    .table-border{
        border: 1px solid black;
        border-collapse: collapse;
    }
    .table tfoot tr:last-child td{
         padding-top:10px;
         }
</style>
</head>
<body>
    <div id="myslip" name="slip" class="slip">
        <div style="text-align:center">
            <img src="{% static 'images/slogo.png' %}" style="display: block; height: 60px; border: 0; margin:auto;"> <br>
            <div>SANKEY  SOLUTIONS PVT. LTD</div>
            <div>602, Windsor Commerce Building,Baner Road, Baner, Pune Maharashtra 411045</div>
            <div>Salary slip - {{slip.month}} {{slip.year}} </div>
        </div>
        <br>
        <div style="border: 1px solid black; margin: 2px;" class="table-border">
            <table style="margin-bottom:1%; width: 100%;" cellpadding='4' cellspacing='4'>
                <tr>{{slip.}}
                    <td class="bold-text">Employe Id:</td>
                    <td>{{slip.emp_id}}</td>
                    <td class="bold-text">DOJ:</td>
                    <td>{{slip.sankey_date_of_joining}}</th>
                </tr>
                <tr >
                    <td class="bold-text">Employee Name:</td>
                    <td>{{slip.emp_name}}</td>
                    <td class="bold-text">UAN No:</td>
                    <td>{{slip.uan_number}}</td>
                </tr>
                <tr>
                    <td class="bold-text">Designation:</td>
                    <td>{{slip.employee_designation}}</td>
                    <td class="bold-text">ESIC No:</td>
                    <td>{{slip.pesic}}</td>
                </tr>
                <tr>
                    <td class="bold-text">Total Present Days:</td>
                    <td>{{slip.total_present_days}}</td>
                    <td class="bold-text">Bank A/C No:</td>
                    <td>{{slip.account_no}}</td>
                </tr>
                <tr>
                    <td class="bold-text">Total Working Days:</td>
                    <td>{{slip.total_working_days}}</td>
                    <td class="bold-text">PAN No:</td>
                    <td>{{slip.pancard}}</td>
                </tr>
            </table>
        </div>
        <br><br>

        <div style="margin: 2px;" class="table-border">
            <table style="margin-bottom:1%; width: 100%;"  cellpadding="4" cellspacing="0">
                <tr  style="border: 2px black solid;"  >
                    <th class="table-border">Earnings</th>
                    <th class="table-border">Amount</th>
                    <th class="table-border">Deductions</th>
                    <th class="table-border">Amount</th>
                </tr> 
                <tr>
                    <td class="table-border">Basic</td>
                    <td class="table-border right">{{slip.basic_salary}}</td>
                    <td class="table-border">Provident Fund</td>
                    <td class="table-border right">{{slip.provident_fund}}</td>
                </tr>
                <tr>
                    <td class="table-border">HRA</td>
                    <td class="table-border right">{{slip.hra_salary}}</td>
                    <td class="table-border">ESIC</td>
                    <td class="table-border right">{{slip.mesic}}</td>
                </tr>
                <tr>
                    <td class="table-border">Travel Allowance</td>
                    <td class="table-border right">{{slip.traveling_allowance}}</td>
                    <td class="table-border">Professional Tax</td>
                    <td class="table-border right">{{slip.professional_tax}}</td>
                </tr>
                <tr>
                    <td class="table-border ">Medical Allowance</td>
                    <td class="table-border right">{{slip.medical_allowance}}</td>
                    <td class="table-border">Other Charges</td>
                    <td class="table-border right">{{slip.other_charges}}</td>
                </tr>
                <tr>
                    <td  class="table-border">Other Allowance</td>
                    <td  class="table-border right">{{slip.other_allowance}}</td>
                    <td  class="table-border">TDS</td>
                    <td  class="table-border right">{{slip.tds}}</td>
                </tr>

                <tr>
                    <td  class="table-border">Arrears</td>
                    <td  class="table-border right">{{slip.arrears}}</td>
                    <td class="table-border">Advances</td>
                    <td class="table-border right">{{slip.advance}}</td>
                </tr>

                <tr class="">
                    <td  class="table-border">Leave Encashment</td>
                    <td  class="table-border right">{{slip.leave_encashment}}</td>
                    <td  class="table-border"></td>
                    <td  class="table-border right"></td>
                </tr>
                <tr class="">
                    <td  class="table-border ">Bonus</td>
                    <td  class="table-border right">{{slip.bonus}}</td>
                    <td  class="table-border"></td>
                    <td  class="table-border right"></td>
                </tr>
                <tfoot>
                <tr>
                    <td  class="table-border"><b>Total Earnings RS.</b></td>
                    <td   class="table-border right"><b>{{slip.gross_salary}}</b></td>

                    <td   class="table-border"><b>Total Deductions RS.</b></td>
                    <td   class="table-border right"><b>{{slip.total_deduction}}</b></td>
                </tr>
                <tr>
                    <td  ></td>
                    <td  ></td>
                    <td   class="table-border"><b>Net Pay:</b></td>
                    <td   class="table-border right"><b>{{slip.salary_in_hand}}</b></td>
                </tr>
            </tfoot>
            </table>
        </div>
    </div>
    <div class="print"> <button onclick="downloadPDF()">Print</button>
    </div>
  
</body>
</html> 


"""