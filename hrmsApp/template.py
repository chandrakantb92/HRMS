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
            <!-- <img src="{% static 'images/slogo.png' %}" style="display: block; height: 60px; border: 0; margin:auto;"> <br> -->
            <div> <h2> <b>SANKEY  SOLUTIONS PVT. LTD</b> </h2> </div>
            <div><h3> <b>602, Windsor Commerce Building,Baner Road, Baner, Pune Maharashtra 411045 </b> </h3></div>
            <div><h3>Salary slip : month - year </h4></div>
        </div>
        <br>
        <div style="border: 1px solid black; margin: 2px;" class="table-border">
            <table style="margin-bottom:1%; width: 100%;" cellpadding='4' cellspacing='4'>
                <tr>
                    <td class="bold-text">Employe Id:</td>
                    <td> emp_id </td>
                    <td class="bold-text">DOJ:</td>
                    <td> sankey_date_of_joining </th>
                </tr>
                <tr >
                    <td class="bold-text">Employee Name:</td>
                    <td> emp_name </td>
                    <td class="bold-text">UAN No:</td>
                    <td> uan_number </td>
                </tr>
                <tr>
                    <td class="bold-text">Designation:</td>
                    <td> employee_designation </td>
                    <td class="bold-text">ESIC No:</td>
                    <td> pesic </td>
                </tr>
                <tr>
                    <td class="bold-text">Total Present Days:</td>
                    <td> total_present_days </td>
                    <td class="bold-text">Bank A/C No:</td>
                    <td> account_no </td>
                </tr>
                <tr>
                    <td class="bold-text">Total Working Days:</td>
                    <td> total_working_days </td>
                    <td class="bold-text">PAN No:</td>
                    <td> pancard </td>
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
                    <td class="table-border right"> basic_salary </td>
                    <td class="table-border">Provident Fund</td>
                    <td class="table-border right"> provident_fund </td>
                </tr>
                <tr>
                    <td class="table-border">HRA</td>
                    <td class="table-border right"> hra_salary </td>
                    <td class="table-border">ESIC</td>
                    <td class="table-border right">  mesic </td>
                </tr>
                <tr>
                    <td class="table-border">Travel Allowance</td>
                    <td class="table-border right"> traveling_allowance </td>
                    <td class="table-border">Professional Tax</td>
                    <td class="table-border right"> professional_tax </td>
                </tr>
                <tr>
                    <td class="table-border ">Medical Allowance</td>
                    <td class="table-border right"> medical_allowance </td>
                    <td class="table-border">Other Charges</td>
                    <td class="table-border right"> other_charges </td>
                </tr>
                <tr>
                    <td  class="table-border">Other Allowance</td>
                    <td  class="table-border right"> other_allowance </td>
                    <td  class="table-border">TDS</td>
                    <td  class="table-border right"> tds </td>
                </tr>

                <tr>
                    <td  class="table-border">Arrears</td>
                    <td  class="table-border right"> arrears </td>
                    <td class="table-border">Advances</td>
                    <td class="table-border right"> advance </td>
                </tr>

                <tr class="">
                    <td  class="table-border">Leave Encashment</td>
                    <td  class="table-border right"> leave_encashment </td>
                    <td  class="table-border"></td>
                    <td  class="table-border right"></td>
                </tr>
                <tr class="">
                    <td  class="table-border ">Bonus</td>
                    <td  class="table-border right"> bonus </td>
                    <td  class="table-border"></td>
                    <td  class="table-border right"></td>
                </tr>
               
                <tr>
                    <td  class="table-border"><b>Total Earnings RS.</b></td>
                    <td   class="table-border right"><b> gross_salary </b></td>

                    <td   class="table-border"><b>Total Deductions RS.</b></td>
                    <td   class="table-border right"><b> total_deduction </b></td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td class="table-border"><b>Net Pay:</b></td>
                    <td   class="table-border right"><b> salary_in_hand </b></td>
                </tr>
            </tfoot>
            </table>
        </div>
    </div>
    </div>
  
</body>
</html> 
"""


form16_template = """
<!DOCTYPE html>
<html>
<style>
    html{
    font-family: 'Times New Roman';
    font-size: 14px;
    line-height: 110%;
    }
    table {
        width: 100%;
        border-collapse: collapse;
    }
    .main-table td{
        font-weight: 0px; 
        border: 1px solid black;
        padding: 8px;
    }
    .main-table th{
        border: 1px solid black; 
    }
    .top-table td{
        width: 100%;
        border: 1px solid black;
        border-collapse: collapse;
        text-align: center;
    }
    .custom-table {
        border-collapse: collapse;
    }
    .custom-table th,
    .custom-table td {
        padding: 5px;
        text-align: left;
    }
    .custom-table th {
        border: 1px solid black;
    }
    .custom-table td {
        border-left: 1px solid black;
        border-right: 1px solid black; 
    }
    .custom-table tr:first-child th {
        border-top: 1px solid black;
    }
    .custom-table tr:last-child td {
        border-bottom: 1px solid black;
    }
    .custom-table td:first-child {
        width: 60%;
    }
    /* .custom-table td:nth-last-child(3) {
        width: 10%;
        text-align: left;
    } */
    .custom-table td:nth-last-child(2) {
        width: 20%;
        text-align: right;
    }
    .custom-table td:nth-last-child(1) {
        width: 20%;
        text-align: right;
    }
    .custom-table td {
        padding-left: 20px;
    }
    .last-table table {
        width: 100%;
        margin: 0 auto;
        border-collapse: collapse;
        border: 1px solid black;
    }
    .last-table th,
    .last-table td {
        padding: 8px;
        border: 1px solid black;
    }
    .last-table td:nth-child(1){
        text-align: center;
    }
    .last-table td:nth-child(1){
        text-align: center;
    }
   .last-table th:nth-child(1) {
        width: 5%;
    }
   .last-table th:nth-child(2) {
        width: 60%;
    }
   .last-table th:nth-child(3) {
        width: 35%;
    }
    .last-table th:nth-child(1) {
        width: 5%;
    }
    .signature {
        display: flex;
        border: 1px solid #000;
        justify-content: center;
    }
    .firstTable td{
        text-align: center;
        font-size: 16px;
        border-bottom: none;
    }
    .secondTable td{
        width: 25%;
        text-align: left;
        border-bottom: none;
    }
   .thirdTable td{
    width: 50%;
    text-align: center;
    border-bottom: none;
   }
   .fourthTable th{
    width: 25%;
   }
   .fourthTable td{
    text-align: center;
   }
   .fifthTable td{
    text-align: center;
    border-top: none;
   }
   .sixthTable td{
    border-bottom: none;
    border-top: none;
    text-align: center;
   }
   .seventhTable th{
    width: 20%;
   }
   .seventhTable td:nth-child(1)
   {
    text-align: left;
   }
   .seventhTable td:nth-child(2)
   {
    text-align: left;
   }
   .seventhTable td{
    text-align: right;
   }
   .eightthTable td:first-child{
    text-align: center;

   }
   .eightthTable td{
    text-align: right;

   }
   .eightthTable th{
    /* border-bottom: none; */
    border-top: none;
   }
   .ninethTable td{
    text-align: center;
   }
   .ninethTable th{
    text-align: center;
   }
   .tenthTable td{
    border-bottom: none;
   }
   .pageNum{
    color: black; 
    font-weight:bold;
    font-size: 14px;
    text-align: right;
    margin-top: 30px;
   }
   .left td:nth-child(1) {
    text-align:left;
   }
   .left td:nth-child(2) {
    text-align:left;
   }
   .center{
    text-align:center;
   }
   .tfleft td:nth-child(3){
    text-align:left;
   }
   .tfleft td:nth-child(4){
    text-align:left;
   }

   .center-head th:nth-child(1) {
    text-align:center;
   }
   .center-head th:nth-child(2) {
    text-align:center;
   }
   .center-head th:nth-child(3) {
    text-align:center;
   }
   .center-head th:nth-child(4) {
    text-align:center;
   }
   .center{
    text-align:center;
   }

</style>
<body>
    <table class="main-table firstTable" >
        <tr>
            <td> <b>FORM NO.16</b></td>
        </tr>
        <tr>
            <td style="font-size: 14px;">[See rule31(1)(a)]</td>
        </tr>
        <tr>
            <td><b>PART A </b> </td>
        </tr>
        <tr >
            <td style="font-size: 14px;"><b> Certificate under section 203 of the Income-tax Act, 1961 for Tax deducted at source on Salary</b></td>
        </tr>
    </table>
    <table class="main-table secondTable">  
        <tr>
            <td>Certificate No.</td>
            <td></td>
            <td>Last Update On.</td>
            <td></td>
        </tr>
    </table>

    <table class="main-table thirdTable">  
        <tr>
            <td><strong> Name and address of employer:</strong></td>
            <td><strong>Name and designation of the employee:</strong></td>
        </tr>
        <tr>
            <td style="text-align: left;">company_name<br/> company_address </td>
            <td style="text-align: left;">employee_name <br/> employee_designation </td>
        </tr>
    </table>

    <table class="main-table fourthTable" >  
       
        <tr class="center-head">
            <th> PAN No. of the Deductor</th>
            <th> TAN of the Deductor</th>
            <th> PAN No. of the Employee</th>
            <th> Employee Reference No. Provided by the Employer (if available)</th>
        </tr>
          <tr  >
            <td> deductor_pan </td>
            <td> duductor_tan </td>
            <td> employee_pan </td>
            <td> emp_id </td>
          </tr>
    </table>

    <table class="main-table fifthTable">
        <tr >
            <td rowspan="3" style="width: 50%;"><Strong>CIT (TDS)</Strong></td>
            <td rowspan="2"><Strong>Assessment year</Strong></td>
            <td colspan="2"><Strong>Period with the Employer</Strong></td>
        </tr>
        <tr>
            <td style="width: 18%;"><Strong>From</Strong></td>
            <td style="width: 12;" ><Strong>To</Strong></td>
        </tr>
        <tr style="border-right: 1px solid #333;">
        <td> assessment_year </td>
        <td > from_year </td>
        <td > to_year</td>
        </tr>
    </table>

    <table class="main-table sixthTable">
        <tr >
            <td><strong>
                Summary of amount paid/credited and tax deducted at source there on in respect of the employee</strong>
            </td>
        </tr>
    </table>
    <table class="main-table seventhTable">
        <tr>
            <th>Quarter(s)</th>
            <th>Receipt Numbers of<br/> 
                original quarterly <br/>
                statements of TDS<br/>
                 under <br/>
                 sub-section (3) of <br/>
                 section 200</th>
            <th>Amount paid/credited</th>
            <th>Amount of tax deducted ( Rs.)</th>
            <th>Amount of tax deposited/ remitted (Rs.)</th>
        </tr>
        <tr>
            <td>Quarter 1</td>
            <td>Non-Filling</td>
            <td> value_zero </td>
            <td> value_zero </td>
            <td> value_zero </td>
        </tr>
        <tr>
            <td>Quarter 2</td>
            <td>Non-Filling</td>
            <td> value_zero </td>
            <td> value_zero </td>
            <td> value_zero </td>
        </tr>
        <tr>
            <td>Quarter 3</td>
            <td>Non-Filling</td>
            <td> value_zero </td>
            <td> value_zero </td>
            <td> value_zero </td>
        </tr>
        <tr>
            <td>Quarter 4</td>
            <td>Non-Filling</td>
            <td> value_zero </td>
            <td> value_zero </td>
            <td> value_zero </td>
        </tr>
        <tr>
           <td style="text-align: center;"><b>Total (Rs.)</b></td>
            <td></td>
            <td><b> value_zero </b></td>
            <td><b> value_zero </b></td>
            <td><b> value_zero </b></td>
            
        </tr>
    </table>
    <table  class="main-table fifthTable">
        <tr>
            <td>
               <b> I. DETAILS OF TAX DEDUCTED AND DEPOSITED IN THE CENTRAL GOVERNMENT ACCOUNT THROUGH<br/>
                BOOK ADJUSTMEN</b><br/>
                (The deductor to provide payment wise details of tax deducted and deposited with respect to the deductee)
            </td>
        </tr>
    </table>

    <table class="main-table eightthTable">
        <tr>
            <th  class="center" rowspan="2" style="width: 10%;">Sr. No.</th>
            <th rowspan="2">Tax Deposited in respect on of the deductee (Rs.)</th>
            <th colspan="4">Book identification number (BIN)</th>
        </tr>

        <tr>
            <th>Receipt numbers of form No. 24G</th>
            <th>DDO Sequence Number in Form No. 24G</th>
            <th>Date of Transfer Voucher (dd/mm/yyyy)</th>
            <th>Status of matching with Form No.24G</th>
        </tr>

        <tr style="border-right: 1px solid #000;">
           <td style="text-align: center;"><b>TOTAL</b></td>
            <td><b> value_zero </b></td>
            <td></td>
            <td></td>
            <td></td>
            <td> value_zero </td>
        </tr>
    </table>
    <table class="main-table fifthTable">
        <tr>
            <td>
                <b> II. DETAILS OF TAX DEDUCTED AND DEPOSITED IN THE CENTRAL GOVERNMENT ACCOUNT THROUGH<br/>
                    CHALLAN</b><br/>
                 (The deductor to provide payment wise details of tax deducted and deposited with respect to the deductee)
             </td>
        </tr>
    </table>

    <table class="main-table eightthTable">
        <tr>
            <th  class="center" rowspan="2" style="width: 10%;">Sr. No.</th>
            <th rowspan="2" style="width: 22%;">Tax Deposited in respect on of the employee (Rs.)</th>
            <th colspan="4">Challan identification number (CIN)</th>
        </tr>

        <tr>
            <th>BSR Code of the <br/>Bank Branch</th>
            <th>Date on which tax <br/>deposited(dd/mm/y)</th>
            <th>Challan Serial Number</th>
            <th>Status of matching <br/>with OLTAS</th>
        </tr>

        <tr style="border-right: 1px solid #000;">
           <td class="center"><b>TOTAL</b></td>
            <td><b> value_zero </b></td>
            <td></td>
            <td></td>
            <td></td>
            <td> value_zero </td>
        </tr>
    </table>

    <table class="main-table">
        <tr>
            <td style="text-align: center; border-top: none;"><strong> Verification</strong></td>
        </tr>
        <tr>
            <td style="border-bottom: none;"> <strong>I, SANDEEP RAJARAM PATIL, son of RAJARAM PATIL working in the capacity of DIRECTOR do hereby certify that a
                sum of Rs.0.00/ has been deducted at source and paid to the credit of the Central Government. I further certify that the
                information given above is true and correct based on the books of account, documents and other available records.</strong></td>
        </tr>
    </table>

    <table class="main-table ninethTable ">
        <tr class="left">
            <td class="left-align"><strong> Place </strong></td>
            <td class="left-align"> verification_place </td>
            <td rowspan="2" style="padding-top: 40px;"><strong> verification_signature <br> (Signature of person responsible for deduction of tax)</strong></td>
        </tr>
        <tr  class="left">
            <td class="left-align"><b>Date</b></td>
            <td class="left-align"> verification_date </td>
        </tr>
        <tr class="left">
            <td class="left-align"><b>Designation</b></td>
            <td class="left-align"> verification_designation </td>
            <td><b>Full Name: </b> verification_full_name </td>
        </tr>
    </table><br/><br/><br/><br/><br/>

    <table class="pageNum">
        <tr>
          <!-- Add Page Numbering in HTML using &p; and &P -->
          <td>Page <span >1</span> of <span>4</span> 
          </td>
       </tr>
    </table>
    <pre>
    
    
    
    </pre>

    <h4><b>Notes:</b></h4>
    <ol type="1" style="text-align: justify; line-height: 30px;">
        <li>Government deductors to fill information in item I if tax is paid without production of an income-tax
            challan and in item II if tax is paid accompanied by an income-tax challan.</li>
        <li>Non-Government deductors to fill information in item II.</li>
        <li>The deductor shall furnish the address of the Commissioner of Income-tax (TDS) having jurisdiction as
            regards TDS statements of the assessee.</li>
        <li>If an assessee is employed under one employer only during the year, certificate in Form No. 16 issued for
            the quarter ending on 31st March of the financial year shall contain the details of tax deducted and
            deposited for all the quaters of the financial year.</li>
        <li>If an assessee is employed under more than one employer during the year, each of the employers shall issue
            Part A of the certificate in Form No. 16 pertaining to the period for which such assessee was employed with
            each of the employers. Part B (Annexure) of the certificate in Form No.16 may be issued by each of the
            employers or the last employer at the option of the assessee.</li>
        <li>In items I and II, in column for tax deposited in respect of deductee, furnish total amount of TDS and
            education cess.</li>

    </ol>

    <table class="top-table">
        <tr>
            <td><strong> PART B (Annexure)</strong></td>
        </tr>
        <tr>
            <td>Details of Salary paid and any other income and tax deducted</td>
        </tr>
    </table>
    <table class="custom-table">
        <tr>
            <td>1. Gross Salary </td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (a) Salary as per provisions contained in section 17(1)</td>
            <td> gross_salary </td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (b) Value of perquisites under section 17(2) (as per Form No. 12BA, <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; wherever
                applicable)
            </td>
            <td> value_zero </td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (c) Profits in lieu of salary under section 17(3) (as per Form No. <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 12BA,
                wherever applicable)
            </td>
            <td> value_zero </td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (d) Total</td>
            <td>&nbsp;</td>
            <td> total_gross_salary </td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (e) Reported total amount of salary received from other employer(s)</td>
            <td> other_employer_reported_total_amount </td>
            <td>&nbsp; </td>
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td>2. Less: Allowance to the extent exempt under section 10 </td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (a) Travel concession or assistance under section 10(5)</td>
            <td> value_zero </td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (b) Death-cum-retirement gratuity under section 10(10)
            </td>
            <td> value_zero </td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;&nbsp;&nbsp;&nbsp; (c) Commuted value of pension under section 10(10A)
            </td>
            <td> value_zero </td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (d) Cash equivalent of leave salary encashment under section 10 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (10AA)</td>
            <td> value_zero </td>
            <td>&nbsp;</td>
        </tr>
        <tr style="border-bottom: 1px solid #FFFFFF;">
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (e) House rent allowance under section 10(13A)</td>
            <td> hra_allowance </td>
            <td>&nbsp; </td>
        </tr>
        <tr style="border-top: 1px solid #000;">
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (f) Amount of any other exemption under section 10
                <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Note: Break-up to be prepared by employer and
                issued to the <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; employee, where applicable, before
                furnishing of Part B to the &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; employee]
            </td>
            <td>value_zero </td>
            <td>&nbsp; </td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (g) Total amount of any other exemption under section 10</td>
            <td>value_zero </td>
            <td>&nbsp; </td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (h) Total amount of exemption claimed under section 10
                <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [2(a)+2(b)+2(c)+2(d)+2(e)+2(g)]
            </td>
            <td>&nbsp; </td>
            <td> total_exemption_claim </td>
            
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td>3. Total amount of salary received from current employer [1(d)-2(h)] </td>
            <td>&nbsp;</td>
            <td><strong> total_salary_amount </strong></td>
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td>4. Less: Deductions under section 16 </td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (a) Standard deduction under section 16(ia)</td>
            <td> standard_deducation </td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (b) Entertainment allowance under section 16(ii)</td>
            <td> value_zero </td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (c) Tax on employment under section 16(iii)
            </td>
            <td> professional_tax </td>
            <td>&nbsp;</td>
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td>5. Total amount of deductions under section 16 [4(a)+4(b)+4(c)] </td>
            <td>&nbsp;</td>
            <td> total_deducation </td>
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td>6. Income chargeable under the head "Salaries" [(3+1(e)-5)] </td>
            <td>&nbsp;</td>
            <td>income_chargeable</td>
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td>7. Add: Any other income reported by the employee </td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (a) Income (or admissible loss) from house property reported by <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; employee
                offered for TDS</td>
            <td>income_house_property</td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (b) Income under the head Other Sources offered for TDS</td>
            <td>value_zero</td>
            <td>&nbsp;</td>
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td >8. Total amount of other income reported by the employee [7(a)+7 &nbsp;&nbsp;&nbsp;&nbsp; (b)] </td>
            <td>&nbsp;</td>
            <td>total_employee_income_reported</td>
        </tr>
        <tr style="border-top: 1px solid #000;">
            <td >9. Gross total income (6+8)</td>
            <td>&nbsp;</td>
            <td><strong>gross_income</strong></td>
        </tr>
    </table>
    <pre>
    
    
    
    </pre>
    <pre>
    
    
    
    
    </pre>
    <table class="pageNum">
        <tr>
          <td>Page <span >2</span> of <span>4</span> 
          </td>
       </tr>
    </table>
    <pre>
    
    </pre>
    
    <table class="custom-table"><br/>
    
        <tr style="border-top: 1px solid #000;">
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>Deductible Amount</td>
        </tr>
        <tr style="border-top: 1px solid #000;">
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (a) Deduction in respect of life insurance premia, <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; contributions to provident
                fund etc. under section 80C</td>
            <td>&nbsp;</td>
            <td>life_insurance_deducation</td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (b) Deduction in respect of contribution to certain pension <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; funds under
                section 80CCC</td>
            <td>&nbsp;</td>
            <td>pension_fund_deducation</td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (c) Deduction in respect of contribution by taxpayer to <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; pension scheme under
                section 80CCD (1)
            </td>
            <td>&nbsp;</td>
            <td>taxpayer_pension_deducation</td>
        </tr>
        <tr style="border-top: 1px solid #000;">
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (d) Total deduction under section 80C, 80CCC and 80CCD &nbsp; (1)
            </td>
            <td>&nbsp;</td>
            <td> total_section_deduction </td>
        </tr>
        <tr style="border-top: 1px solid #000;">
            <td style="padding-left: none"> &nbsp;&nbsp;&nbsp;&nbsp; Note: 1. Aggregate amount deductible under section
                80C, <br/>&nbsp;&nbsp;&nbsp; 80CCC and 80CCD (1) shall not exceed one lakh and <br/>&nbsp;&nbsp;&nbsp; fifty thousand rupees.
            </td>
            <td>&nbsp;</td>
            <td>&nbsp; </td>
        </tr>

        <tr style="border: 1px solid #000;">
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (e) Deductions in respect of amount paid/deposited to  <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; notified pension scheme
               under section 80CCD (1B)
            </td>
            <td>&nbsp;</td>
            <td> deducation_of_80ccd_1b </td>
        </tr>

        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (f) Deduction in respect of contribution by Employer to <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; pension scheme under
                section 80CCD (2)</td>
            <td>&nbsp;</td>
            <td> deducation_of_80ccd_2 </td>
        </tr>
        <tr >
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (g) Deduction in respect of health insurance premia under <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; section 80D (2)</td>
            <td>&nbsp;</td>
            <td> deducation_of_80d </td>
        </tr>
        <tr >
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (h) Deduction in respect of interest on loan taken for higher <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; education under
                section 80E</td>
            <td>&nbsp;</td>
            <td> deducation_of_80e </td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (i) Total Deduction in respect of donations to certain funds, <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;charitable
                institutions, etc. under section 80G</td>
            <td>&nbsp;</td>
            <td> deducation_of_80g </td>
        </tr>
        <tr style="border-bottom:1px solid #333">
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (j) Deduction in respect of interest on deposits in savings <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; account under
                section 80TTA</td>
            <td>&nbsp;</td>
            <td> deducation_of_80tta </td>
        </tr>
        <tr style="border-top:1px solid #333">
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (k) Amount deductible under any other provision(s) of <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Chapter VI-A <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Note:
                Break-up to be prepared by employer and issued <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; to the employee, where applicable, before furnishing of
                <br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Part B to the employee]</td>
            <td>&nbsp;</td>
            <td> duduction_of_other_provision </td>
        </tr>
        <tr>
            <td> &nbsp;&nbsp;&nbsp;&nbsp; (l) Total of amount deductible under any other provision(s) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; of Chapter VI-A
            </td>
            <td>&nbsp;</td>
            <td> total_amount_deducation_of_other_provision </td>
        </tr>

        <tr>
            <td> &nbsp;&nbsp; Note: 1. Aggregate amount deductible under section 80C,<br/>&nbsp;&nbsp;&nbsp; 80CCC and 80CCD (1) shall not
                exceed one lakh and fifty <br/>&nbsp;&nbsp;&nbsp; thousand rupees.</td>
            <td>&nbsp;</td>
            <td>&nbsp; </td>
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td >10. Aggregate of deductible amount under Chapter VIA  [10(d)+10 (e)+10(f)+10(g)+10(h)+10(i)+10(j)+10(l)]
            </td>
            <td >&nbsp;</td>
            <td ><strong> aggregate_deductible_amount </strong></td>
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td >11. Total income (9-10) </td>
            <td >&nbsp;</td>
            <td> total_income </td>
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td >12. Tax on total income </td>
            <td >&nbsp;</td>
            <td> tax_on_income </td>
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td >13. Education Cess @4% (on tax computated at S.No.12) </td>
            <td >&nbsp;</td>
            <td> education_cess </td>
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td >14. Tax payable (12+13) ( Less Rebate u/s 87A Rs.0.00) </td>
            <td >&nbsp;</td>
            <td> tax_payable_less_rebate </td>
        </tr>
    </table>

    <table class="custom-table tenthTable">
        <tr>
            <td >15. Less: Relief under section 89 </td>
            <td >&nbsp;</td>
            <td> relief_amount </td>
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td >16. Tax payable (14-15) </td>
            <td >&nbsp;</td>
            <td><strong> final_payable </strong></td>
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td style="text-align: center;"><strong>Verification</strong></td>
        </tr>
    </table>

    <table class="custom-table">
        <tr>
            <td style="text-align: left;"><strong>I SANDEEP RAJARAM PATIL, son of RAJARAM PATIL working in the capacity
                    of DIRECTOR do hereby certify that the information given above is true, complete and correct and is
                    based on the books of account, documents, TDS statements and other available records.</strong></td>
        </tr>
    </table>

    <table class="main-table ninethTable">
        <tr  class="left">
            <td class="left-align"><strong> Place </strong></td>
            <td class="left-align">verification_place</td>
            <td rowspan="2" style="padding-top: 40px;"><strong>&nbsp; <br/> (Signature of person responsible for deduction of tax)</strong></td>
        </tr>
        <tr class="left">
            <td class="left-align"><b>Date</b></td>
            <td class="left-align"> verification_date </td>
        </tr>
        <tr class="left">
            <td class="left-align"><b>Designation</b></td>
            <td class="left-align"> verification_designation </td>
            <td><b>Full Name: </b> verification_full_name </td>
        </tr>
    </table>

    <!-- <br/><br><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/> -->
    <pre>
    </pre>
    <table class="pageNum">
        <tr>
          <!-- Add Page Numbering in HTML using &p; and &P -->
          <td style="padding-top: 13%;">Page <span >3</span> of <span>4</span> 
          </td>
       </tr>
    </table><br/><br/>
    <pre>
    
    </pre>
    <!-- 4th page Start -->
    <br/><br><br/><br/>
    <table class="last-table">
        <tr>
            <td colspan="3" style="font-size: 16px;"><strong> Tax Deducted Summary </strong></td>
        </tr>
        <tr>
            <td colspan="3">(Summary of Tax Payable and Tax Deducted Information)</td>
        </tr>
        <tr class="center-head">
            <th>Sr. No.</th>
            <th style="font-size: 13px;">Particular</th>
            <th style="font-size: 13px;">Amount</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Tax payable as per Part-B (Sr. No 16) </td>
            <td style="text-align: right;">0</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Tax Deducted at Current Employment </td>
            <td style="text-align: right;">0</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Tax Deducted at Previous Employment </td>
            <td style="text-align: right;">0</td>
        </tr>
        <tr>
            <td> 4</td>
            <td>Total Tax Deducted (2 + 3) </td>
            <td style="text-align: right;">0</td>
        </tr>
        <tr>
            <td>5</td>
            <td><strong>Net Tax Payable / (Refundable) (1 – 4) </strong></td>
            <td style="text-align: right;">0</td>
        </tr>
    </table>
    <br>
    <table class="main-table ninethTable">
        <tr  class="left">
            <td class="left-align"><strong> Place </strong></td>
            <td class="left-align">Thane</td>
            <td rowspan="2" style="padding-top: 40px;"><strong>(Signature of person responsible for deduction of tax)</strong></td>
        </tr>
        <tr class="left">
            <td class="left-align"><b>Date</b></td>
            <td class="left-align">01/12/2022</td>
        </tr>
        <tr class="left">
            <td class="left-align"><b>Designation</b></td>
            <td class="left-align">DIRECTOR</td>
            <td class="left-align"><b>Full Name: </b>SANDEEP RAJARAM PATIL</td>
        </tr>
    </table>
    
    <!-- <br/><br><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
    <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/> -->
    <table class="pageNum">
      <tr>
        <td style="padding-top: 60%;">Page <span >4</span> of <span>4</span> 
        </td>
     </tr>
  </table>
</body>
</html>
"""