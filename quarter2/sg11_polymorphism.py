class Patient: #create a parent class for all of the patients
    def __init__(self, name, bill_amount): # __init__ constructor so we can set the name and bill amount. The double underscore indicates that it is a private attribute
        self.__name = name #assign name as a private attribute
        self.__bill_amount = bill_amount # assign bill amount to a private attribute

    def get_name(self): # getter method so that we can safely retrieve/read the value of a private or restricted object attribute (the name)
        return self.__name #return the private name attribute
    def get_bill_amount(self): # define a method to get the bill amount 
        return self.__bill_amount #return the private bill amount attribute

    def set_name (self, name): #setter method so we can update/change the patient's name if needed
        self.__name = name #this replaces the current private name attribue with the new value provided
    def set_bill_amount(self, bill_amount): #setter method so that we can update/change the patient's bill amount
        self.__bill_amount = bill_amount #this replaces the current private bill_amount attribute with the new value provided

    def calculate_bill(self): #this defines a method so that we can compute and also return the final bill for a regular patient
        return self.__bill_amount #this returns the original bill amount the same since regular patients don't receive any discounts

    def display_patient_type(self): #defines a method so that we can print the classification/category of the patient (regular patient dor this class)
        print("Patient Type: Regular Patient") #prints the statement which states that this patient is a regular patient

class SeniorPatient(Patient): #defines a child class named SeniorPatient which inherits from the all the attributes and methods from the parent class (Patient Class)
    def calculate_bill(self): #this overrides the parent's calculate_bill method so that we can apply the senior citizen rule (which is the 20% discount)
        return self.get_bill_amount()*0.80 #returns/retrieves the bill amount and mutiplies it by 0.80 so that we can apply a 20% discount for senior patients

    def display_patient_type(self): #this overrifes the parent's display_patient_type method for the senior citizen patients
        print("Patient Type: Senior Citizen") #prints the statement saying that this patient is a senior citizen

class PhilHealthPatient(Patient): #defines another child class that is named PhilHealthPatient. This class also inherits the attributes and methods from the parent class (Patient class)
    def calculate_bill(self): #this overrides the parent's calculate_bill method so that we can apply the PhilHealth member rules (which is the 15% discount)
        return self.get_bill_amount()*0.85 #retrieves/returns the bill amount and multiplies it by 0.85 so that we can apply the 15% discount for PhilHealth patients

    def display_patient_type(self): #this overrides the parent's display_patient_type method for PhilHealth patients
        print("Patient Type: PhilHealth Member") #this prints the statement which indicates that this patient is a PhilHealth patient


print("Hospital Billing System") #this is the header/title
print("-----------------------") #this is the line that acts as a separator (similar to the one in the sample output given in the sg11-polymorphism activity 1)

p1=Patient("Juan Dela Cruz", 15000.00) #this instantiates a regular Patient object named "p1" with a name and also bill
print("Patient Name: ", p1.get_name()) #prints a label (Patient Name: ) and also retrieves Juan's name using the get_name() or getter method
p1.display_patient_type() #this calls the display_patient_typw() method on "p1" so that it can print "Patient Type: Regular Patient"
print("Original Bill: ₱", p1.get_bill_amount()) #prints "Original Bill" and also retrieves Juan's original bill amount using get_bill_amount or getter method
print("Final Bill: ₱", p1.calculate_bill()) #prints "Final Bill: " and calculates Juan's fina bill amount using the calculate_bill()
print() #this is tocreate an empty blank to separate or add space before the next patient

p2=SeniorPatient("Maria Santos", 15000.00) #this instantiates a SeniorPatient object that is named "p2" with a name and bill
print("Patient Name: ", p2.get_name()) #prints "Patient Name: " and also retrieves Maria's name using the inherited get_name() or getter method
p2.display_patient_type() #calls the display_patient_type method to be able to print the "Patient Type: Senior Citizen"
print("Original Bill: ₱", p2.get_bill_amount()) # prints "Original Bill: " and also retrieves Maria's name using the inherited get_name() method
print("Final Bill: ₱", p2.calculate_bill()) #calls the calculate_bill() method to compute and also print the 20% discounted total for senior citizens.
print() #prints an empty blank line to separate from the next patient

p3=PhilHealthPatient("Pedro Reyes", 15000.00) #this instantiates a PhilHealthPatient object named "p3" with a name and bill
print("Patient Name: ", p3.get_name()) #prints ("Patient Name: ") and retrieves Pedro's name using the inherited get_name() method
p3.display_patient_type() #calls the display_patient_type() method to print "Patient Type: PhilHealth Member"
print("Original Bill: ₱", p3.get_bill_amount()) # prints "Original Bill: " and retrieve Pedro's original bill amount using the get_bill_amount()
print("Final Bill: ₱", p3.calculate_bill()) #calls the calculate_bill() method to compute and also to print the 15% discounted total for PhilHealth patients

