
initial_population = 8_191_988_453
growth_rate = 0.009
years = 100

print(f"{'Year':<6} {'Population':<15} {'Increase':<15}")
print("-" * 40)


for year in range(1, years + 1):

    population = initial_population * (1 + growth_rate) ** year
    increase = population - initial_population * (1 + growth_rate) ** (year - 1)

    print(f"{year:<6} {population:,.0f}  {increase:,.0f}")
