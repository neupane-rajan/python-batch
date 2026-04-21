my_dict = {1: "hello", 2: "hi", 3: "bye", "4": "namaste"}

print(my_dict.items())

new = {y: x for x, y in my_dict.items()}
print(new)


country_code = {
    "Nepal": "NP",
    "India": "IN",
    "United States": "US",
    "Germany": "DE",
    "France": "FR",
    "United Kingdom": "GB",
    "Canada": "CA",
    "Australia": "AU",
    "Brazil": "BR",
    "Mexico": "MX",
    "Spain": "ES",
    "Italy": "IT",
    "South Korea": "KR",
    "China": "CN",
    "Japan": "JP",
}
