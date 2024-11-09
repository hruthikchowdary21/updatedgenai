from abc import ABC, abstractmethod

# Abstraction: Creating an abstract class for InsurancePolicy
class InsurancePolicy(ABC):
    # Abstract method to calculate premium, to be defined by subclasses
    @abstractmethod
    def calculate_premium(self):
        pass

    # Abstract method to provide policy details, to be defined by subclasses
    @abstractmethod
    def get_policy_details(self):
        pass

# Class: Blueprint for creating insurance policy objects
class HealthInsurancePolicy(InsurancePolicy):
    # Encapsulation: Using __ to make attributes private
    def __init__(self, policy_id, holder_name, age, health_conditions):
        self.__policy_id = policy_id
        self.__holder_name = holder_name
        self.__age = age
        self.__health_conditions = health_conditions

    # Encapsulation: Public method to access the private attribute __policy_id
    def get_policy_id(self):
        return self.__policy_id

    # Method to calculate premium based on age and health conditions
    def calculate_premium(self):
        base_premium = 5000  # Base premium amount in dollars
        if self.__age > 45:
            base_premium += 2000  # Additional charge for age
        if len(self.__health_conditions) > 0:
            base_premium += 1000 * len(self.__health_conditions)  # Charge per health condition
        return base_premium

    # Method to get policy details
    def get_policy_details(self):
        details = f"Policy ID: {self.__policy_id}, Holder: {self.__holder_name}, Age: {self.__age}, Conditions: {self.__health_conditions}"
        return details

# Inheritance: Creating a new class that inherits from HealthInsurancePolicy
class SeniorCitizenPolicy(HealthInsurancePolicy):
    # Additional discount for senior citizens
    def calculate_premium(self):
        premium = super().calculate_premium()  # Call the parent's calculate_premium method
        discount = 0.1 * premium  # 10% discount for senior citizens
        return premium - discount

# Polymorphism: Different policy types have their own implementations of calculate_premium
def print_policy_info(policy):
    # Using polymorphism: The same method can work with different types of policies
    print(policy.get_policy_details())
    print(f"Calculated Premium: ${policy.calculate_premium()}\n")

# Object creation: Creating instances of HealthInsurancePolicy
basic_policy = HealthInsurancePolicy(
    policy_id="H12345",
    holder_name="John Doe",
    age=40,
    health_conditions=["diabetes"]
)

# Object creation: Creating instances of SeniorCitizenPolicy
senior_policy = SeniorCitizenPolicy(
    policy_id="S67890",
    holder_name="Jane Smith",
    age=70,
    health_conditions=["hypertension", "arthritis"]
)

# Calling the polymorphic function
print("Basic Policy Information:")
print_policy_info(basic_policy)  # Works with HealthInsurancePolicy object

print("Senior Citizen Policy Information:")
print_policy_info(senior_policy)  # Works with SeniorCitizenPolicy object
