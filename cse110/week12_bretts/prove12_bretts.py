# Enter the year of interest: 1959
# Enter the country of interest: 1959

# The overall max life expectancy is: 86.751 from Monaco in 2019
# The overall min life expectancy is: 17.76 from Iceland in 1882

# For the year 1959:
# The average life expectancy across all countries was 54.95
# The max life expectancy was in Norway with 73.49
# The min life expectancy was in Mali with 28.077

import os
os.system("cls")

year_request = input("Enter the year of interest: ")
country2_request = input("Enter the country of interest: ").title()

# Pull in File
with open("life-expectancy.csv") as f:

    max_life = 0
    max_life_country = ""
    max_life_year = 0
    min_life = 150
    min_life_country = ""
    min_life_year = 0
    max_life_country_request = ""
    max_life_request = 0
    min_life_country_request = ""
    min_life_request = 150
    max_life_year_request2 = ""
    max_life_request2 = 0
    min_life_year_request2 = ""
    min_life_request2 = 150
    request_country = []
    request_life = []
    request2_year = []
    request2_life = []

    next(f)
    for line in f:

        # Strip & Clean
        clean_line = line.strip()
        parts = clean_line.split(",")

        # Assign Parts
        country_name = parts[0]
        country_code = parts[1]
        year = parts[2]
        life_expectancy = float(parts[3])

        # Filters
        if life_expectancy > max_life:
            max_life = life_expectancy
            max_life_country = country_name
            max_life_year = year

        if life_expectancy < min_life:
            min_life = life_expectancy
            min_life_country = country_name
            min_life_year = year

        # List Requested Year
        if year_request == year:
            request_country.append(country_name)
            request_life.append(life_expectancy)

        # List Requested Country
        if country2_request == country_name:
            request2_year.append(year)
            request2_life.append(life_expectancy)

    # Filter Requested Year
    for i in range(len(request_life)):

        if max_life_request <= request_life[i]:
            max_life_request = request_life[i]
            max_life_country_request = request_country[i]

        if min_life_request >= request_life[i]:
            min_life_request = request_life[i]
            min_life_country_request = request_country[i]

    # Calc Requested Year Average
    avg_life_request = sum(request_life) / len(request_life)

    # Filter Requested Country
    for i in range(len(request2_life)):

        if max_life_request2 <= request2_life[i]:
            max_life_request2 = request2_life[i]
            max_life_year_request2 = request2_year[i]

        if min_life_request2 >= request2_life[i]:
            min_life_request2 = request2_life[i]
            min_life_year_request2 = request2_year[i]

    # Calc Requested Country Average
    avg_life_request2 = sum(request2_life) / len(request2_life)

    # Output
    print()
    print(
        f"The overall max life expectancy is: {max_life} from {max_life_country} in {max_life_year}")
    print(
        f"The overall min life expectancy is: {min_life} from {min_life_country} in {min_life_year}")
    print()
    print(f"For the year {year_request}:")
    print(
        f"The average life expectancy across all countries was {float(avg_life_request):.2f}")
    print(
        f"The max life expectancy was in {max_life_country_request} with {max_life_request}")
    print(
        f"The min life expectancy was in {min_life_country_request} with {min_life_request}")
    print()
    print(f"For the country {country2_request}:")
    print(
        f"The average life expectancy across all years was {float(avg_life_request2):.2f}")
    print(
        f"The max life expectancy in {max_life_year_request2} was {max_life_request2}")
    print(
        f"The min life expectancy in {min_life_year_request2} was {min_life_request2}")
    print()
