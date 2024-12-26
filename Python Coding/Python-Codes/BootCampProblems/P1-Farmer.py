# Define the land segments and their respective crops
land_segments = {
    "tomatoes": 80 / 5,
    "potatoes": 80 / 5,
    "cabbage": 80 / 5,
    "sunflower": 80 / 5,
    "sugarcane": 80 / 5
}

# Define the yield and selling price for each crop
crop_yield = {
    "tomatoes": (0.3 * land_segments["tomatoes"] * 10 + 0.7 * land_segments["tomatoes"] * 12) * 1000,  # in kg
    "potatoes": land_segments["potatoes"] * 10 * 1000,  # in kg
    "cabbage": land_segments["cabbage"] * 14 * 1000,  # in kg
    "sunflower": land_segments["sunflower"] * 0.7 * 1000,  # in kg
    "sugarcane": land_segments["sugarcane"] * 45  # in tonnes
}

selling_price = {
    "tomatoes": 7,  # per kg
    "potatoes": 20,  # per kg
    "cabbage": 24,  # per kg
    "sunflower": 200,  # per kg
    "sugarcane": 4000  # per tonne
}

# Calculate the overall sales
overall_sales = sum(crop_yield[crop] * selling_price[crop] for crop in crop_yield if crop != "sugarcane") + \
                crop_yield["sugarcane"] * selling_price["sugarcane"]

# Calculate the sales realisation from chemical-free farming at the end of 11 months
chemical_free_sales = sum(crop_yield[crop] * selling_price[crop] for crop in ["tomatoes", "potatoes", "cabbage", "sunflower"])

# Print the results
print(f"Overall sales achieved by Mahesh from the 80 acres of land: Rs. {overall_sales}")
print(f"Sales realisation from chemical-free farming at the end of 11 months: Rs. {chemical_free_sales}")