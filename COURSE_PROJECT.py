
#   Cynthia Daniels
#   CIS261
#   Project Phase 2
from datetime import datetime
# 
def GetEmpName():
    empname = input("Enter employee name (END to terminate): ")
    return empname
def GetDatesWorked():
    #write the code to input fromdate and todate and return the values from the function.  
    #Prompt the user for the dates in the following format: mm/dd/yyyy
    #no validations are needed for this input, we will assume the dates are entered correctly
    startdate = str(input("Enter start date (mm/dd/yy): "))
    fromdate = datetime.strptime(startdate, '%m/%d/%y')
    enddate = str(input("Enter end date (mm/dd/yy): "))
    todate = datetime.strptime(enddate, '%m/%d/%y')
    return fromdate, todate
    



def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours


def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate


def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate


def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay




def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    # the following code creates a for loop to read through EmpDetailList and assign values in list to variables
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        
        #write code to assign values to todate, empname, hours, hourlyrate, and taxrate from EmpLst
        


        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        # the following line of code assigns TotEmployees totals to dictionary 
        EmpTotals["TotEmp"] = TotEmployees
        # write code to assign TotHours, TotGrossPay, TotTax, and TotNetPay to corresponding dictionary item

        EmpTotals["TotHrs"] = TotHours
        EmpTotals["TotGP"] = TotGrossPay
        EmpTotals["TotTAX"] = TotTax
        EmpTotals["TotNP"] = TotNetPay
        




def PrintTotals(EmpTotals):    
    print()
    # use dictionary to print totals
    # the following line of code prints Total Employees from the dictionary
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    
    # write code to print TotalHrs, TotGrossPay, TotTax and TotNetPay from dictionary
    print(f'Total Hours Worked: {EmpTotals["TotHrs"]}')
    print(f'Total Gross Pay: {EmpTotals["TotGP"]}')
    print(f'Total Tax: {EmpTotals["TotTAX"]}')
    print(f'Total Net Pay : {EmpTotals["TotNP"]}')




if __name__ == "__main__":
 

    #create empty list and dictionary
    EmpDetailList = []
    EmpTotals = {}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        else:
            fromdate, todate = GetDatesWorked()
            hours = GetHoursWorked()
            hourlyrate = GetHourlyRate()
            taxrate = GetTaxRate()
       

       
       #write code to insert fromdate, todate, empname, hours, hourlyrate, and taxrate into list EmpDetail
   
        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]

        
        
        #the following code appends the list EmpDetail to the list EmpDetailList
        EmpDetailList.append(EmpDetail)

     
    printinfo(EmpDetailList)
    PrintTotals (EmpTotals)