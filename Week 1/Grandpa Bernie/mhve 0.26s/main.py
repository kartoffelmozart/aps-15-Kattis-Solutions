n = int(input())
country_to_year = {}
for _ in range(n):
    country,year = input().split()
    if country not in country_to_year:
        country_to_year[country] = []
    country_to_year[country].append(int(year))
for country in country_to_year:
    country_to_year[country].sort()
output_list = []
q = int(input())
for _ in range(q):
    country,k = input().split()
    output_list.append(str(country_to_year[country][int(k) - 1]))
print('\n'.join(output_list))