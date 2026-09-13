# Save this file inside: backend/simple_interest.py

class SimpleInterestCalculator:
    """
    Engine module for calculating Simple Interest values.
    Designed to serve individual or combined outputs for UI rendering.
    """
    
    def __init__(self, principal: float, annual_rate: float, time_years: float):
        """
        Initializes the calculator state with user inputs.
        
        :param principal: The initial sum of money invested or borrowed (P).
        :param annual_rate: The annual interest rate as a percentage (R, e.g., 5.5 for 5.5%).
        :param time_years: The length of the investment/loan term in years (T).
        """
        self.principal = float(principal)
        self.rate_decimal = float(annual_rate) / 100.0
        self.time_years = float(time_years)

    def get_interest_only(self) -> float:
        """
        Calculates and returns ONLY the absolute interest earned or owed.
        Formula: I = P * R * T
        """
        interest = self.principal * self.rate_decimal * self.time_years
        return round(interest, 2)

    def get_total_amount(self) -> float:
        """
        Calculates and returns the final total maturity amount (Principal + Interest).
        Formula: A = P * (1 + R * T)
        """
        total_amount = self.principal * (1.0 + (self.rate_decimal * self.time_years))
        return round(total_amount, 2)
