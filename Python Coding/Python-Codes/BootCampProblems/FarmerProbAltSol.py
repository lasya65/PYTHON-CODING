# Constants
total_land = 80  # in acres
segments = 5
land_per_segment = total_land / segments

# Yield and price per crop
tomato_yield_30 = 10  # tonnes per acre for 30% of the land
tomato_yield_70 = 12  # tonnes per acre for 70% of the land
tomato_price_per_kg = 7  # Rs per kg

potato_yield = 10  # tonnes per acre
potato_price_per_kg = 20  # Rs per kg

cabbage_yield = 14  # tonnes per acre
cabbage_price_per_kg = 24  # Rs per kg

sunflower_yield = 0.7  # tonnes per acre
sunflower_price_per_kg = 200  # Rs per kg

sugarcane_yield = 45  # tonnes per acre
sugarcane_price_per_tonne = 4000  # Rs per tonne

# Calculate sales for each crop
tomato_sales = (0.3 * land_per_segment * tomato_yield_30 * 1000 * tomato_price_per_kg) + \
               (0.7 * land_per_segment * tomato_yield_70 * 1000 * tomato_price_per_kg)

potato_sales = land_per_segment * potato_yield * 1000 * potato_price_per_kg
cabbage_sales = land_per_segment * cabbage_yield * 1000 * cabbage_price_per_kg
sunflower_sales = land_per_segment * sunflower_yield * 1000 * sunflower_price_per_kg
sugarcane_sales = land_per_segment * sugarcane_yield * sugarcane_price_per_tonne

# Overall sales
overall_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales

# Sales realization from chemical-free farming at the end of 11 months
chemical_free_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales

# Output the results
print(f"Overall sales achieved by Mahesh from the 80 acres of land: Rs. {overall_sales}")
print(f"Sales realization from chemical-free farming at the end of 11 months: Rs. {chemical_free_sales}")