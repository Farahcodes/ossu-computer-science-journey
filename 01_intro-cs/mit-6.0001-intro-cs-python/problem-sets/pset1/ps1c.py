# Problem C: Finding the Best Savings Rate
# This script calculates the best annual savings rate needed to reach a target down payment for a house.
# It uses a bisection search algorithm to find the minimum rate of return required within a specified tolerance.

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial savings: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
house_cost = 800000.0
down_payment_portion = 0.25
target_down_payment = house_cost * down_payment_portion
months = 36 # 3 years
savings_tolerance = 100.0

# Define the target savings window
min_target_savings = target_down_payment - savings_tolerance
max_target_savings = target_down_payment + savings_tolerance

r = None  # Final annual rate of return
steps = 0 # Number of bisection search steps

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################

# Case 1: Initial deposit is already high enough (or more) for the lower bound of the savings goal.
# Problem note specifies r=0.0 in this scenario.
if initial_deposit >= min_target_savings:
    r = 0.0
    # steps remains 0 as no bisection search is performed.
else:
    # Case 2: Check if it's impossible to reach even the lower bound of the target window
    # with the maximum possible rate of return (100%).
    savings_at_max_rate = initial_deposit * (1 + 1.0 / 12)**months
    if savings_at_max_rate < min_target_savings:
        r = None
        # steps remains 0 as no bisection search is performed.
    else:
        # Case 3: Bisection search is needed to find the lowest r.
        low_r_bound = 0.0
        high_r_bound = 1.0
        best_r_found_in_search = None

        # Epsilon for r convergence in bisection.
        # Chosen to achieve a balance of r-precision and step count (~12 steps).
        epsilon_r_convergence = 0.00025

        # Max iterations for safety, though epsilon should cause break earlier.
        for iteration_count in range(100):
            steps += 1 # Count this bisection iteration
            current_guess_r = (low_r_bound + high_r_bound) / 2.0

            current_savings = initial_deposit * (1 + current_guess_r / 12)**months

            if current_savings >= min_target_savings and current_savings <= max_target_savings:
                # Found a valid r; store it and try for an even lower r.
                best_r_found_in_search = current_guess_r
                high_r_bound = current_guess_r
            elif current_savings < min_target_savings:
                # Savings too low; rate needs to be higher.
                low_r_bound = current_guess_r
            else: # current_savings > max_target_savings
                # Savings too high (overshot window); rate needs to be lower.
                high_r_bound = current_guess_r

            # Stop if the search interval for r is sufficiently small.
            if (high_r_bound - low_r_bound) < epsilon_r_convergence:
                break

        r = best_r_found_in_search
        # If best_r_found_in_search is still None, 'r' will correctly be None.
        # 'steps' will hold the number of bisection iterations performed.

##################################################################################################
## Print the results ##
##################################################################################################
print(f"Best savings rate: {r}")
print(f"Steps in bisection search: {steps}")